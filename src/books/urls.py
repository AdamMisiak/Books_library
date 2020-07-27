from django.urls import path
from .views import book_results_view, book_add_view, find_book_view

app_name = 'books'

urlpatterns = [
	#path('', book_results_view, name='index'),
	path('add/', book_add_view, name='add'),
	path('find/', find_book_view, name='find'),
	path('results/', book_results_view, name='results'),
]