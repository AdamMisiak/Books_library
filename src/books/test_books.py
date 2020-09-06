import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from .functions import books_finder
from .models import Book, BookPosition
from .forms import BookForm


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

    @pytest.mark.django_db
    def test_book_labels(self):
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

        title_label = test_book._meta.get_field("title").verbose_name
        author_label = test_book._meta.get_field("author").verbose_name
        image_label = test_book._meta.get_field("image").verbose_name
        sites_label = test_book._meta.get_field("sites").verbose_name
        description_label = test_book._meta.get_field("description").verbose_name
        genre_1_label = test_book._meta.get_field("genre_1").verbose_name

        assert title_label == "title"
        assert author_label == "author"
        assert image_label == "image"
        assert sites_label == "sites"
        assert description_label == "description"
        assert genre_1_label == "genre 1"


class TestBookPositionModel:
    @pytest.mark.django_db
    def test_book_position_create(self):
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
        test_book_position = BookPosition.objects.create(
            user=test_user,
            book=test_book,
            value="Add",
            month="June",
            year=2020,
            status="Done",
            review="Great",
        )

        assert BookPosition.objects.count() == 1
        assert str(BookPosition.objects.get(id=1).user) == "adam"
        assert str(BookPosition.objects.get(id=1).book) == "title"
        assert BookPosition.objects.get(id=1).value == "Add"
        assert BookPosition.objects.get(id=1).month == "June"
        assert BookPosition.objects.get(id=1).year == 2020
        assert BookPosition.objects.get(id=1).status == "Done"
        assert BookPosition.objects.get(id=1).review == "Great"
        assert isinstance(test_book_position, BookPosition)

    @pytest.mark.django_db
    def test_book_position_labels(self):
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
        test_book_position = BookPosition.objects.create(
            user=test_user,
            book=test_book,
            value="Add",
            month="June",
            year=2020,
            status="Done",
            review="Great",
        )

        user_label = test_book_position._meta.get_field("user").verbose_name
        book_label = test_book_position._meta.get_field("book").verbose_name
        value_label = test_book_position._meta.get_field("value").verbose_name
        month_label = test_book_position._meta.get_field("month").verbose_name
        year_label = test_book_position._meta.get_field("year").verbose_name
        review_label = test_book_position._meta.get_field("review").verbose_name

        assert user_label == "user"
        assert book_label == "book"
        assert value_label == "value"
        assert month_label == "month"
        assert year_label == "year"
        assert review_label == "review"


class TestBookForm:
    def test_book_form_title_field_label(self):
        form = BookForm()
        assert form.fields['title'].label is None or form.fields['title'].label == 'Title'
