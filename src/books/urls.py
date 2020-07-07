from django.urls import path
from .views import book_results_view, book_add_view, book_add_view

app_name = ' books'

urlpatterns = [
	path('', book_results_view, name='book_list'),
	path('add/', book_add_view, name='book_add'),
	path('book_add_view/', book_add_view, name='like'),
]