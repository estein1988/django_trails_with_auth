# Generated by Django 3.1.4 on 2020-12-10 21:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='users',
            field=models.ManyToManyField(related_name='users', through='django_app.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
