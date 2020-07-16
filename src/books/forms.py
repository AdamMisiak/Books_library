from django import forms
from .models import Book


class BookForm(forms.ModelForm):
	title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Book title"}))
	author = forms.CharField(label='Author', widget=forms.TextInput(attrs={"placeholder": "Book author"}))
	sites = forms.CharField(label='Sites', widget=forms.TextInput(attrs={"placeholder": "Number of sites"}))
	genre_1 = forms.CharField(label='Genre', widget=forms.TextInput(attrs={"placeholder": "Book genre"}))

	class Meta:
		model = Book
		fields = [
			'title',
			'author',
			'sites',
			'genre_1',
		]


class SearchingForm(forms.Form):
	title = forms.CharField(label='Title')

	class Meta:
		model = Book
		fields = [
			'title',
		]
