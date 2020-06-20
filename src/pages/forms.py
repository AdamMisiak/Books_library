from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


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
