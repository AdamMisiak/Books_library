from django.urls import path
from .views import book_add_view, book_options_view

app_name = 'pages'

urlpatterns = [
	path('delete_book/', book_add_view, name='book_add'),

]