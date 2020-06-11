from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm


def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):

	context = {
	}
	return render(request, 'contact.html', context)


def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		return redirect('/')
	contex = {
		'form':form
	}
	return render(request, 'users/register.html', contex)
