import pytest
from datetime import datetime
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from .models import UserImage
from .forms import (
    RegisterForm,
    UpdateForm,
    NavbarSearchingForm,
    BookOptionsForm,
    BookUpdateForm,
    ImageUpdateForm,
    ReviewBookForm,
)
from .choices import GENRE_CHOICES, MONTH_CHOICES, STATUS_CHOICES


@pytest.fixture
def login_user():
    client = Client()
    logged_in = client.login(username="adam", password="adam")
    return logged_in


class TestPagesViews:
    @pytest.mark.django_db
    def test_home_view_status_code(self, client):
        client = Client()
        url = reverse("home")
        response = client.get(url)
        assert response.status_code == 200

    def test_about_view_status_code(self, client):
        client = Client()
        url = reverse("about")
        response = client.get(url)
        assert response.status_code == 200

    def test_register_view_status_code(self, client):
        client = Client()
        url = reverse("users:register")
        response = client.get(url)
        assert response.status_code == 200

    def test_login_view_status_code(self, client):
        client = Client()
        url = reverse("users:login")
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_account_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:account")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_user_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:update")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_library_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:library")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_info_book_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:info_book")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_book_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:update_book")
            response = client.get(url)
            assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_image_view_status_code(client, login_user):
        User.objects.create_user("adam", "adam@test.com", "adam")
        if login_user:
            url = reverse("users:update_image")
            response = client.get(url)
            assert response.status_code == 200


class TestUserModel:
    @pytest.mark.django_db
    def test_user_create(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        assert User.objects.count() == 1
        assert User.objects.get(id=1).email == "adam@test.com"
        assert User.objects.get(id=1).username == "adam"
        assert isinstance(test_user, User)

    @pytest.mark.django_db
    def test_default_user_is_active(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        assert test_user.is_active

    @pytest.mark.django_db
    def test_user_labels(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        email_label = test_user._meta.get_field("email").verbose_name
        username_label = test_user._meta.get_field("username").verbose_name
        password_label = test_user._meta.get_field("password").verbose_name

        assert email_label == "email address"
        assert username_label == "username"
        assert password_label == "password"


class TestUserImageModel:
    @pytest.mark.django_db
    def test_user_create(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        test_user_image = UserImage.objects.create(user=test_user)

        assert UserImage.objects.count() == 1
        assert str(UserImage.objects.get(id=1).user) in "<User: adam>"
        assert UserImage.objects.get(id=1).image == "images/user.png"
        assert isinstance(test_user_image, UserImage)

    @pytest.mark.django_db
    def test_user_image_labels(self):
        test_user = User.objects.create_user("adam", "adam@test.com", "adam")
        test_user_image = UserImage.objects.create(user=test_user)
        user_label = test_user_image._meta.get_field("user").verbose_name
        image_label = test_user_image._meta.get_field("image").verbose_name

        assert user_label == "user"
        assert image_label == "image"


class TestRegisterForm:
    def test_register_form_fields_labels(self):
        form = RegisterForm()
        assert (
            form.fields["username"].label is None
            or form.fields["username"].label == "Username"
        )
        assert (
            form.fields["email"].label is None
            or form.fields["email"].label == "Email address"
        )
        assert (
            form.fields["password1"].label is None
            or form.fields["password1"].label == "Password"
        )
        assert (
            form.fields["password2"].label is None
            or form.fields["password2"].label == "Password confirmation"
        )

    def test_register_form_fields_help_texts(self):
        form = RegisterForm()
        assert (
            form.fields["username"].help_text
            == "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
        assert form.fields["email"].help_text == ""
        assert (
            form.fields["password1"].help_text
            == "<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        )
        assert (
            form.fields["password2"].help_text
            == "Enter the same password as before, for verification."
        )


class TestUpdateForm:
    def test_update_form_fields_labels(self):
        form = UpdateForm()
        assert (
            form.fields["username"].label is None
            or form.fields["username"].label == "Username"
        )
        assert (
            form.fields["email"].label is None
            or form.fields["email"].label == "Email address"
        )

    def test_update_form_fields_help_texts(self):
        form = UpdateForm()
        assert (
            form.fields["username"].help_text
            == "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
        assert form.fields["email"].help_text == ""


class TestNavbarSearchingForm:
    def test_navbar_search_form_fields_labels(self):
        form = NavbarSearchingForm()
        assert (
            form.fields["title"].label is None or form.fields["title"].label == "Title"
        )

    def test_navbar_search_form_fields_help_texts(self):
        form = NavbarSearchingForm()
        assert form.fields["title"].help_text == ""


class TestBookOptionsForm:
    def test_book_options_form_fields_labels(self):
        form = BookOptionsForm()
        assert form.fields["id"].label is None or form.fields["id"].label == "id"

    def test_book_options_form_fields_help_texts(self):
        form = BookOptionsForm()
        assert form.fields["id"].help_text == ""


class TestBookUpdateForm:
    def test_book_update_form_fields_labels(self):
        today = datetime.now()
        current_month = today.month
        current_year = today.year

        form = BookUpdateForm()
        assert (
            form.fields["genre"].label is None or form.fields["genre"].label == "Genre"
        )
        assert form.fields["genre"].choices[0] == GENRE_CHOICES[0]
        assert form.fields["genre"].initial == ("Financials", "Financials")
        assert "Select" in str(form.fields["genre"].widget)

        assert (
            form.fields["month"].label is None or form.fields["month"].label == "Month"
        )
        assert form.fields["month"].choices[0] == MONTH_CHOICES[0]
        assert str(MONTH_CHOICES[current_month - 1]) in str(
            form.fields["month"].initial
        )
        assert "Select" in str(form.fields["month"].widget)

        assert form.fields["year"].label is None or form.fields["year"].label == "Year"
        assert str(current_year) in str(form.fields["year"].initial)

        assert (
            form.fields["status"].label is None
            or form.fields["status"].label == "Status"
        )
        assert form.fields["status"].choices[0] == STATUS_CHOICES[0]
        assert "In progress" in str(form.fields["status"].initial)
        assert "Select" in str(form.fields["status"].widget)

    def test_book_update_form_fields_help_texts(self):
        form = BookUpdateForm()
        assert form.fields["genre"].help_text == ""
        assert form.fields["month"].help_text == ""
        assert form.fields["year"].help_text == ""
        assert form.fields["status"].help_text == ""


class TestImageUpdateForm:
    def test_image_update_form_fields_labels(self):
        form = ImageUpdateForm()
        assert (
            form.fields["image"].label is None or form.fields["image"].label == "Image"
        )

    def test_image_update_form_fields_help_texts(self):
        form = ImageUpdateForm()
        assert form.fields["image"].help_text == ""


class TestReviewBookForm:
    def test_review_book_form_fields_labels(self):
        form = ReviewBookForm()
        assert (
            form.fields["review"].label is None
            or form.fields["review"].label == "Review"
        )

    def test_review_book_form_fields_help_texts(self):
        form = ReviewBookForm()
        assert form.fields["review"].help_text == ""
