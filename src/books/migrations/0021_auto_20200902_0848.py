# Generated by Django 3.0.8 on 2020-09-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0020_auto_20200901_1553"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookposition",
            name="review",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
