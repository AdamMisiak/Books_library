from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.apps import apps
Book = apps.get_model('books', 'Book')


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]


class UpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
		]


class BookOptions(forms.ModelForm):
	id = forms.IntegerField(label='Id', widget=forms.TextInput(attrs={"placeholder": "Book id"}))

	class Meta:
		model = Book
		fields = [
			'id'
		]
