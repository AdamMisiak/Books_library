# Generated by Django 3.0.8 on 2020-09-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0018_auto_20200901_0746"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookposition",
            name="review",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
