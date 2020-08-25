import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from .functions import books_finder
from .models import Book


@pytest.fixture
def login_user():
    client = Client()
    logged_in = client.login(username="adam", password="adam")
    return logged_in


class TestBooksViews:
    @pytest.mark.django_db
    def test_find_book_view_status_code(self, client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("books:find")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_results_book_view_status_code(self, client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("books:results")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_find_failed_view_status_code(self, client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("books:find_failed")
            response = client.get(url)
            assert response.status_code == 200


class TestBooksFunctions:
    def test_books_finder(self):
        result = books_finder("Wspomnienia Gracza Giełdowego")
        assert type(result) == list
        assert type(result[0]) == dict
        assert result[0]["id"].isnumeric() == True
        assert "Wspomnienia Gracza Giełdowego" in result[0]["title"]


class TestBookModel:
    @pytest.mark.django_db
    def test_book_create(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        test_book = Book.objects.create(
            id=1,
            title="title",
            author="author",
            image="image",
            sites=10,
            description="description",
            genre_1="genre",
        )
        test_book.user.add(test_user)

        assert Book.objects.count() == 1
        assert Book.objects.get(id=1).title == "title"
        assert Book.objects.get(id=1).author == "author"
        assert Book.objects.get(id=1).image == "image"
        assert Book.objects.get(id=1).sites == 10
        assert Book.objects.get(id=1).description == "description"
        assert Book.objects.get(id=1).genre_1 == "genre"
        assert str(Book.objects.get(id=1).user.all()) in "<QuerySet [<User: adam>]>"
        assert (
            str(User.objects.get(id=1).books_added.all())
            in "<QuerySet [<Book: title>]>"
        )
        assert isinstance(test_book, Book)
