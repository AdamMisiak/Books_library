from django.shortcuts import render
from .models import Book

# Create your views here.
def book_detail_view(request):
	book = Book.objects.get(id=1)
	contex = {
		'book':book

	}
	return render(request, 'books/book_detail.html', contex)
