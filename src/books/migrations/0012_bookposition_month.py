# Generated by Django 3.0.8 on 2020-07-11 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_bookposition'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookposition',
            name='month',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
