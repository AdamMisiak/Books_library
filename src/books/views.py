from django.shortcuts import render
from .models import Book

# Create your views here.
def book_detail_view(request):
	book = Book.objects.get(id=1)
	contex = {
		'title': book.title,
		'author': book.author,
		'sites': book.sites,


	}
	return render(request, 'book.html', contex)
