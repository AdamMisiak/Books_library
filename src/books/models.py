from django.db import models


# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	sites = models.IntegerField()
	genre_1 = models.CharField(max_length=100)
	genre_2 = models.CharField(max_length=100, blank=True)
