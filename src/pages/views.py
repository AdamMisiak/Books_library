from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):

	context = {
	}
	return render(request, 'contact.html', context)
