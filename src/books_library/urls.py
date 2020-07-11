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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pages.views import home_view, contact_view
from books.views import book_results_view, find_book_view, finding_failed
from pages.views import register_view, login_view, account_view, update_view, library_view, book_options_view
from django.contrib.auth.views import LogoutView
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    #path('book_result/', book_results_view, name='book_result'),
    path('find_book/', find_book_view, name='find_book'),
    path('book_options/', book_options_view, name='book_options'),
    path('finding_failed/', finding_failed, name='finding_failed'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),

    path('library/', library_view, name='library'),

    path('update/', update_view, name='update'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
    path('__debug__', include(debug_toolbar.urls)),
    #path('ajax/', include('books.urls')),

    path('book_result/', include('books.urls', namespace='books'), name='book_result'),
    path('library/', include('pages.urls', namespace='pages'), name='library'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
