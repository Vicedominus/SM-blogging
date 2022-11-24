from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='blank-profile-picture.jpg')
    bio = models.CharField(max_length=280, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)

    def __str__(self):
        return self.user.username

