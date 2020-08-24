# Generated by Django 3.0.8 on 2020-08-10 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pages", "0002_auto_20200808_1428"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userimage",
            name="image",
            field=models.ImageField(default="images/user.png", upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="userimage",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
