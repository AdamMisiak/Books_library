"""books_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view
from books.views import book_results_view, find_book_view
from users.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('book_result/', book_results_view, name='book_result'),
    path('find_book/', find_book_view, name='find_book'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
]
