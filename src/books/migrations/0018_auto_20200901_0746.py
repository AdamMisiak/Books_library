# Generated by Django 3.0.8 on 2020-09-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20200901_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookposition',
            name='month',
            field=models.CharField(blank=True, default='September', max_length=20),
        ),
    ]
