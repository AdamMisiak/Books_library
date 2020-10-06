from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.CharField(
        max_length=300,
        default="https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png",
    )
    sites = models.IntegerField(blank=True, default=0)
    description = models.CharField(max_length=2000, default=None, blank=True)
    genre_1 = models.CharField(max_length=100, blank=True)
    genre_2 = models.CharField(max_length=100, blank=True)
    user = models.ManyToManyField(User, related_name="books_added", blank=True)

    def __str__(self):
        return str(self.title)


BOOK_CHOICES = (
    ("Add", "Add"),
    ("Delete", "Delete"),
)


STATUS_CHOICES = (
    ("To do", "To do"),
    ("In progress", "In progress"),
    ("Done", "Done"),
)

today = datetime.now()
current_year = today.year
current_month = str(today.strftime("%B"))


# MODEL FOR CONNECTING USER WITH BOOK
class BookPosition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    value = models.CharField(choices=BOOK_CHOICES, default="Delete", max_length=10)
    month = models.CharField(blank=True, default=current_month, max_length=20)
    year = models.IntegerField(blank=True, default=current_year)
    status = models.CharField(choices=STATUS_CHOICES, default="To do", max_length=20)
    review = models.TextField(blank=True, null=True, max_length=1000)
    rate = models.PositiveIntegerField(blank=True, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.book)
