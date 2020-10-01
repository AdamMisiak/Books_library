# Generated by Django 3.0.8 on 2020-07-09 14:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0009_auto_20200623_1551"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.CharField(blank=True, default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name="book",
            name="user",
            field=models.ManyToManyField(
                blank=True, related_name="books_added", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="BookPosition",
        ),
    ]
