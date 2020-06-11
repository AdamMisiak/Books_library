from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm


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
			#login(request, user)
			return redirect('/login')
	else:
		form = RegisterForm()

	contex = {
		'form':form
	}
	return render(request, 'users/register.html', contex)


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request, user)
			return redirect('/')
	else:
		form = AuthenticationForm()

	contex = {
		'form':form
	}
	return render(request, 'users/login.html', contex)


