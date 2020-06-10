from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm


def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RegisterForm()
		#return HttpResponseRedirect('/book_result/')
	contex = {
		# 'form':form
	}
	return render(request, 'users/register.html', contex)
