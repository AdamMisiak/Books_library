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
		# form.save()
		# form = BookForm()
		return HttpResponseRedirect('/book_result/')
	contex = {
		'form': form
	}
	return render(request, 'books/find_book.html', contex)


@login_required(login_url="login")
def book_results_view(request):
	form = request.session['form']
	results = books_finder(form['title'])
	# added = request.POST['add_book']
	# SOME JQUERY NEEDED

	book = Book(id=results[0]['id'], title=results[0]['title'], author=results[0]['author'], image=results[0]['image'],
				description=results[0]['description'])
	book.save()
	book.user.add(request.user)

	contex = {
		'form': form,
		'results': results
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
		print(book_id)
		book_object = Book.objects.get(id=book_id)

		print(book_object.author)

		if user.id in book_object.user.all():
			book_object.user.remove(user)
		else:
			book_object.user.add(user)

		# book_position, created = BookPosition.objects.get_or_create(user=user, book=book_id)
		book_position = BookPosition.objects.create(user=user, book=book_object)
		# if not created:
		if book_position.value == "Add":
			book_position.value = "Delete"
		else:
			book_position.value = "Add"

		book_position.save()

	return redirect('books:book_list')
