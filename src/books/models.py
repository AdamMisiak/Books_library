from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
	#dodac swoje id z API
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	image = models.CharField(max_length=300, default='https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png')
	sites = models.IntegerField(blank=True, default=0)
	description = models.CharField(max_length=2000, default=None)
	genre_1 = models.CharField(max_length=100, blank=True)
	genre_2 = models.CharField(max_length=100, blank=True)
	#user = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)#NIE DAWAC ID DO NAZWY BO DJANGO ROBI TO SAMO
	user = models.ManyToManyField(User, related_name='books_added')
