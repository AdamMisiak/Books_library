from django.urls import path
from .views import book_results_view, book_add_view, like

app_name = ' books'

urlpatterns = [
	path('', book_results_view, name='book_list'),
	path('add/', book_add_view, name='book_add'),
	path('like/', like, name='like'),
]