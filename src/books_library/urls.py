from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pages.views import home_view, about_view
import debug_toolbar


urlpatterns = [
    path("books/", include("books.urls")),
    path("users/", include("pages.urls")),
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("admin/", admin.site.urls),
    path("__debug__", include(debug_toolbar.urls)),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
