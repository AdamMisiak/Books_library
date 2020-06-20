from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookForm, SearchingForm
from .functions import books_finder
from .models import Book


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
