from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class R_User(AbstractUser):
    email = models.EmailField(max_length=150)


class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey(R_User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Subreddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    subscriber = models.ManyToManyField(R_User, related_name='user')
    moderator = models.ManyToManyField(Moderator, related_name='moderator')

    def __str__(self):
        return self.name

class Posts(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=4000)
    date_created = models.DateField(default=timezone.now)
    author = models.ForeignKey(R_User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Posts,related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    user = models.ForeignKey(R_User, on_delete=models.CASCADE)
    # upvotes = models.IntegerField(default=0)
    # downvotes = models.IntegerField(default=0)
    # score = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.body

