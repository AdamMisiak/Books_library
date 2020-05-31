from django.shortcuts import render
from .models import Book
from .forms import BookForm


def book_create_view(request):
	form = BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		print(form.cleaned_data)
		form = BookForm()
	contex = {
		'form':form
	}
	return render(request, 'books/book_create.html', contex)


def book_detail_view(request):
	book = Book.objects.get(id=1)
	contex = {
		'book':book

	}
	return render(request, 'books/book_detail.html', contex)
