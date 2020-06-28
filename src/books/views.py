from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookForm, SearchingForm
from .functions import books_finder
from .models import Book, BookPosition


@login_required(login_url="login")
def find_book_view(request):
	form = SearchingForm(request.POST or None)
	if form.is_valid():
		request.session['form'] = form.cleaned_data

		return HttpResponseRedirect('/book_result/')
	contex = {
		'form': form
	}
	return render(request, 'books/find_book.html', contex)


@login_required(login_url="login")
def book_results_view(request):
	form = request.session['form']
	results = books_finder(form['title'])
	for book in results:
		book_id = book['id']
		book_title = book['title']
		book_author = book['author']
		book_image = book['image']
		if book['description'] is None:
			book_description = 'There is no description :('
		else:
			book_description = book['description']

		book = Book(id=book_id, title=book_title, author=book_author, image=book_image,
					description=book_description)
		book.save()

	if 'book_id' in request.session.keys():
		contex = {}
		book_id = request.session['book_id']
		book = Book.objects.get(id=book_id)

		contex['book_position'] = book.user.all


	# SPRAWDZIC TO!
	# print(request.session.keys())
	# if 'book' in request.session.keys():
	# 	contex = {}
	# 	book = request.session['book']
	# 	book_position = BookPosition.objects.get(user=request.user, book=book)
	# 	print(book_position.value)
	# 	contex['book_position'] = book_position


	contex = {
		'form': form,
		'results': results,
	}
	return render(request, 'books/book_result.html', contex)


def book_add_view(request):
	user = request.user
	if request.method == 'POST':
		book_id = request.POST.get('book_id')
		book_title = request.POST.get('book_title')
		book_author = request.POST.get('book_author')
		book_image = request.POST.get('book_image')
		book_description = request.POST.get('book_description')

		book = Book(id=book_id, title=book_title, author=book_author, image=book_image,
					description=book_description)
		book.save()

		request.session['book_id'] = book.id

		if user in book.user.all():
			book.user.remove(user)
		else:
			book.user.add(user)

		# BOOKS AND USER CONNECTION PART
		book_position, created = BookPosition.objects.get_or_create(user=user, book=book)

		if book_position.value == "Add":
			book_position.value = "Delete"
		else:
			book_position.value = "Add"

		book_position.save()

	return redirect('books:book_list')
