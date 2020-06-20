# Generated by Django 3.0.6 on 2020-06-20 08:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0006_auto_20200619_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(related_name='books_added', to=settings.AUTH_USER_MODEL),
        ),
    ]
