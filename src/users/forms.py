from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"placeholder": "Username"}))
	email = forms.CharField(label='Email', required=True,  widget=forms.EmailInput(attrs={"placeholder": "Email"}))
	password = forms.CharField(label='Password', widget=forms.TextInput(attrs={"placeholder": "Password"}))
	#password_confirm = forms.CharField(label='Confirm Password', widget=forms.TextInput(attrs={"Confirm Password"}))

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			# 'password_confirm',
		]
