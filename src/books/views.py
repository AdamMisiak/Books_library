from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
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
	try:
		results = books_finder(form['title'])
	except:
		return render(request, 'books/finding_failed.html')

	for number, book in enumerate(results):
		book_id = book['id']
		book_title = book['title']
		book_author = book['author']
		book_image = book['image']

		if book['description'] is None:
			book_description = 'There is no description :('
		else:
			book_description = book['description']

		results[number]['status'] = 'deleted'
		for book_added in request.user.books_added.all():
			if str(book_id) == str(book_added.id):
				results[number]['status'] = 'added'

		book = Book(id=book_id, title=book_title, author=book_author, image=book_image,
					description=book_description)

		if book not in Book.objects.all():
			book.save()

	contex = {
		'form': form,
		'results': results,
	}

	return render(request, 'books/book_result.html', contex)


def book_add_view(request):
	if request.method == 'GET':
		book_id = request.GET['book_id']
		book = Book.objects.get(id=book_id)
		if request.user in book.user.all():
			book.user.remove(request.user)
			book_position, created = BookPosition.objects.get_or_create(user=request.user, book=book)
			book_position.value = "Delete"
		else:
			book.user.add(request.user)
			book_position, created = BookPosition.objects.get_or_create(user=request.user, book=book)
			book_position.value = "Add"
		book_position.save()

		return HttpResponse('success')
	else:
		return HttpResponse("unsuccesful")


def finding_failed(request, *args, **kwargs):
	return render(request, 'finding_failed.html', {})