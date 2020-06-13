from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm, SearchingForm
from .functions import books_finder
from .models import Book


@login_required(login_url="login")
def find_book_view(request):
	form = SearchingForm(request.POST or None)
	if form.is_valid():
		request.session['form'] = form.cleaned_data
		#form.save()
		#form = BookForm()
		return HttpResponseRedirect('/book_result/')
	contex = {
		'form':form
	}
	return render(request, 'books/find_book.html', contex)


@login_required(login_url="login")
def book_results_view(request):
	form = request.session['form']
	results = books_finder(form['title'])
	# print(results[0]['title'])
	# print(request.user.id)
	book = Book(title=results[0]['title'], author=results[0]['author'], image=results[0]['image'], user_id=request.user)
	book.save()
	#print(book.author, book.title, book.image, book.user_id)	
	contex = {
		'form':form,
		'results':results
	}
	return render(request, 'books/book_result.html', contex)
