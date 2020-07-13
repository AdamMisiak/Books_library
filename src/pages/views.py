from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateForm, BookOptionsForm, BookUpdateForm
from django.apps import apps

# MODELS IMPORTED
Book = apps.get_model('books', 'Book')
BookPosition = apps.get_model('books', 'BookPosition')


# HOME PAGE VIEW
def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
	context = {
	}
	return render(request, 'contact.html', context)


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			return redirect('/login')
	else:
		form = RegisterForm()

	context = {
		'form': form
	}
	return render(request, 'users/register.html', context)


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/')
	else:
		form = AuthenticationForm()

	context = {
		'form': form
	}
	return render(request, 'users/login.html', context)


def account_view(request):
	user = User.objects.get(pk=request.user.id)
	books = user.books_added.all()

	context = {
		'user': user,
		'books': books,
	}
	return render(request, 'users/account.html', context)


def library_view(request):
	user = User.objects.get(pk=request.user.id)
	books = user.books_added.all()
	context = {
		'books': books,
	}
	return render(request, 'users/library.html', context)


def update_view(request):
	if request.method == 'POST':
		user = User.objects.get(pk=request.user.id)
		form = UpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UpdateForm(instance=request.user)
	context = {
		'form': form
	}
	return render(request, 'users/update.html', context)


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


def book_options_view(request):
	if request.method == 'POST':
		form = BookOptionsForm(request.POST)
		if form.is_valid():
			book_id = form.cleaned_data.get('id')
			request.session['book_id'] = book_id

			book = Book.objects.get(id=book_id)
			book_position = BookPosition.objects.get(user=request.user, book=book)

			book_title = book.title
			request.session['book_title'] = book_title

			return render(request, 'users/book_options.html', {'book': book, 'book_position': book_position})


def book_update_view(request):
	if request.method == 'POST':
		form = BookUpdateForm(request.POST)
		if form.is_valid():
			book_id = request.session['book_id']
			book = Book.objects.get(id=book_id)
			book_position = BookPosition.objects.get(user=request.user, book=book)

			genre = form.cleaned_data.get('genre')
			month = form.cleaned_data.get('month')
			book_position.month = month
			book.genre_1 = genre

			book_position.save()
			book.save()
			return redirect('/library')
	else:
		form = BookUpdateForm()

	context = {
		'form': form,
	}

	return render(request, 'users/book_update.html', context)
