from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .choices import GENRE_CHOICES

from django.apps import apps
Book = apps.get_model('books', 'Book')
BookPosition = apps.get_model('books', 'BookPosition')


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


class BookOptionsForm(forms.Form):
	id = forms.IntegerField(label='id')


class BookUpdateForm(forms.Form):
	genre = forms.ChoiceField(label='Genre', choices=GENRE_CHOICES, widget = forms.Select() )
	month = forms.IntegerField(label='Month', widget=forms.TextInput(attrs={"placeholder": "Month of reading"}))
