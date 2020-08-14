import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_book_create():
# 	Book.objects.create_user('title', 'author')
# 	assert Book.objects.count() == 1
# 	assert Book.objects.get(id=1).title == 'title'


def test_find_book_view_status_code(client):
	url = reverse('books:find')
	response = client.get(url)
	assert response.status_code == 302
