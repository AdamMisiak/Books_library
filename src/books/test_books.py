import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from .functions import books_finder


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


class TestBooksFunctions():

	def test_books_finder(self):
		result = books_finder('Wspomnienia Gracza Giełdowego')
		assert type(result) == list
		assert type(result[0]) == dict
		assert result[0]['id'].isnumeric() == True
		assert 'Wspomnienia Gracza Giełdowego' in result[0]['title']