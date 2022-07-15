from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    ID = models.IntegerField(max_length = 3000, primary_key=True)
    Username = models.CharField(max_length=200)
    User_pwd = models.CharField(max_length=200)
    User_email = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Age = models.IntegerField()


class Subreddit(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique= True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    


class Moderator(models.Model):
    ID = models.IntegerField(primary_key=True)
    subreddit_id = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Threads(models.Model):
    ID = models.IntegerField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit_id = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    Post_links = models.URLField(max_length=300)
    post_information = models.CharField(max_length=200)
    post_links_videos = models.URLField(max_length=300)
    post_links_photos = models.URLField(max_length=300)
    time = models.DateTimeField()

class Comments(models.Model):
    ID = models.IntegerField(primary_key=True)
    Thread_id = models.ForeignKey(Threads, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField()

