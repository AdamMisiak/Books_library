import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client


def test_home_view_status_code(client):
	url = reverse('home')
	response = client.get(url)
	assert response.status_code == 200


def test_register_view_status_code(client):
	url = reverse('users:register')
	response = client.get(url)
	assert response.status_code == 200


def test_login_view_status_code(client):
	url = reverse('users:login')
	response = client.get(url)
	assert response.status_code == 200


@pytest.mark.django_db
def test_account_view_status_code(client):
	User.objects.create_user('adam', 'adam@test.com', 'adam')
	client = Client()
	logged_in = client.login(username='adam', password='adam')
	if logged_in:
		url = reverse('users:account')
		response = client.get(url)
		assert response.status_code == 200


@pytest.mark.django_db
def test_update_user_view_status_code(client):
	#need to add feature for logging user
	User.objects.create_user('adam', 'adam@test.com', 'adam')
	client = Client()
	logged_in = client.login(username='adam', password='adam')
	if logged_in:
		url = reverse('users:update')
		response = client.get(url)
		assert response.status_code == 200


@pytest.mark.django_db
def test_user_create():
	User.objects.create_user('adam', 'adam@test.com', 'adam')
	assert User.objects.count() == 1
	assert User.objects.get(id=1).email == 'adam@test.com'
	assert User.objects.get(id=1).username == 'adam'
