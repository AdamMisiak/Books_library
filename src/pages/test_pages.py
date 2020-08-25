import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from .models import UserImage


@pytest.fixture
def login_user():
    client = Client()
    logged_in = client.login(username="adam", password="adam")
    return logged_in


class TestPagesViews:
    def test_home_view_status_code(self, client):
        client = Client()
        url = reverse("home")
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
