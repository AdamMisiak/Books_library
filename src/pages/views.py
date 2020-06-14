from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateForm


def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
	context = {
	}
	return render(request, 'contact.html', context)


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			# login(request, user)
			return redirect('/login')
	else:
		form = RegisterForm()

	contex = {
		'form': form
	}
	return render(request, 'users/register.html', contex)


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/')
	else:
		form = AuthenticationForm()

	contex = {
		'form': form
	}
	return render(request, 'users/login.html', contex)


def account_view(request):
	user = User.objects.get(pk=request.user.id)
	contex = {
		'user': user
	}
	return render(request, 'users/account.html', contex)


def update_view(request):
	user = User.objects.get(pk=request.user.id)
	form = UpdateForm(request.POST)
	if form.is_valid():
		user.username = form.cleaned_data.get('username')
		user.email = form.cleaned_data.get('email')
		form.save()
		return redirect('/account')

	contex = {
		'form': form
	}
	return render(request, 'users/update.html', contex)
