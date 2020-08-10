from datetime import datetime
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .choices import GENRE_CHOICES, MONTH_CHOICES, STATUS_CHOICES
from .models import UserImage

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


# NAVBAR SEARCHING BOOKS FORM
class NavbarSearchingForm(forms.Form):
	title = forms.CharField(label='Title')


# SENDING BOOK ID IN FORM TO BOOK OPTIONS VIEW
class BookOptionsForm(forms.Form):
	id = forms.IntegerField(label='id')


# UPDATING USER'S BOOK INFORMATION
class BookUpdateForm(forms.Form):
	today = datetime.now()
	current_month = today.month

	genre = forms.ChoiceField(label='Genre', choices=GENRE_CHOICES, initial=GENRE_CHOICES[26], widget=forms.Select())
	month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, initial=MONTH_CHOICES[current_month - 1],
							  widget=forms.Select())
	status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES, initial=STATUS_CHOICES[1], widget=forms.Select())


# ADD/UPDATE USER'S IMAGE
class ImageUpdateForm(forms.ModelForm):
	class Meta:
		model = UserImage
		fields = [
			'image'
		]

