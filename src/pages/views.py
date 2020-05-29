from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):

	context = {
		'my_text':'this is about me',
		'my_number':123,
		'my_list':[12,3,4,5,6]

	}
	return render(request, 'contact.html', context)
