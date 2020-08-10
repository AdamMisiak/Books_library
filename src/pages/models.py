from django.db import models
from django.contrib.auth.models import User


class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',
                              default='https://recap-project.eu/wp-content/uploads/2017/02/default-user.jpg')