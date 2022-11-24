from django.db import models
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)
    post_picture = models.ImageField(upload_to='post_pictures', default='react.png')
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def profile_posts(self):
        return self.post_set.all()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.post.title

