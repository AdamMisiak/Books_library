import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User


def test_home_view_status_code(client):
	url = reverse('home')
	response = client.get(url)
	assert response.status_code == 200


def test_register_view_status_code(client):
	url = reverse('register')
	response = client.get(url)
	assert response.status_code == 200


def test_login_view_status_code(client):
	url = reverse('login')
	response = client.get(url)
	assert response.status_code == 200


def test_find_book_view_status_code(client):
	url = reverse('find_book')
	response = client.get(url)
	assert response.status_code == 302


@pytest.mark.django_db
def test_user_create():
	User.objects.create_user('adam', 'adam@test.com', 'adam')
	assert User.objects.count() == 1
	assert User.objects.get(id=1).email == 'adam@test.com'


