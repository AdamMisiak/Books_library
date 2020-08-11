from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import add_book_view, library_view, account_view, register_user_view, login_user_view, update_user_view, \
	info_book_view, update_book_view, update_image_view

app_name = 'users'

urlpatterns = [
	path('delete/', add_book_view, name='delete'),
	path('library/', library_view, name='library'),
	path('account/', account_view, name='account'),
	path('register/', register_user_view, name='register'),
	path('login/', login_user_view, name='login'),
	path('update/', update_user_view, name='update'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('update_image/', update_image_view, name='update_image'),


	path('info_book/', info_book_view, name='info_book'),
	path('update_book/', update_book_view, name='update_book'),
]
