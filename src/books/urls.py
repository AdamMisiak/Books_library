from django.urls import path
from .views import results_book_view, add_book_view, find_book_view, find_book_failed_view

app_name = 'books'

urlpatterns = [
	path('add/', add_book_view, name='add'),
	path('find/', find_book_view, name='find'),
	path('results/', results_book_view, name='results'),
	path('find_failed/', find_book_failed_view, name='find_failed'),

]