# Generated by Django 4.1.3 on 2022-11-19 16:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_alter_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
