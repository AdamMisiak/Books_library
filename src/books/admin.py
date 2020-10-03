from django.contrib import admin
from .models import Book, BookPosition


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre_1", "description")
    list_display_links = ("id", "title")
    list_filter = ("genre_1",)
    search_fields = ("title", "author")
    list_per_page = 20


class BookPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "value", "month", "year", "status", "review")
    list_display_links = ("id", "user")
    list_filter = ("month", "year", "status")
    list_per_page = 20


admin.site.register(Book, BookAdmin)
admin.site.register(BookPosition, BookPositionAdmin)
