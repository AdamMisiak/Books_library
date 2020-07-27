from django.urls import path
from .views import book_add_view, library_view, account_view

app_name = 'users'

urlpatterns = [
	path('delete_book/', book_add_view, name='delete_book'),
	path('library/', library_view, name='library'),
	path('account/', account_view, name='account'),
]