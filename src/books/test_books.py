import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client


# @pytest.mark.django_db
# def test_book_create():
# 	Book.objects.create_user('title', 'author')
# 	assert Book.objects.count() == 1
# 	assert Book.objects.get(id=1).title == 'title'


@pytest.fixture
def login_user():
	client = Client()
	logged_in = client.login(username='adam', password='adam')
	return logged_in


class TestBooksViews:

	@pytest.mark.django_db
	def test_find_book_view_status_code(client, login_user):
		User.objects.create_user('adam', 'adam@test.com', 'adam')
		if login_user:
			url = reverse('books:find')
			response = client.get(url)
			assert response.status_code == 200

	@pytest.mark.django_db
	def test_results_book_view_status_code(client, login_user):
		User.objects.create_user('adam', 'adam@test.com', 'adam')
		if login_user:
			url = reverse('books:results')
			response = client.get(url)
			assert response.status_code == 200

	@pytest.mark.django_db
	def test_find_failed_view_status_code(client, login_user):
		User.objects.create_user('adam', 'adam@test.com', 'adam')
		if login_user:
			url = reverse('books:find_failed')
			response = client.get(url)
			assert response.status_code == 200
