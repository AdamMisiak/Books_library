from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm, SearchingForm



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


def book_results_view(request):
	#book = Book.objects.get(id=1)
	form = request.session['form']
	contex = {
		'form':form,

	}
	return render(request, 'books/book_result.html', contex)
