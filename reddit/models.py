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
    img = models.ImageField(null = True, blank = True, upload_to = 'images/')
    score = models.IntegerField(default=0)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    likes = models.ManyToManyField(R_User, related_name = 'blog_post')
    unlikes = models.ManyToManyField(R_User, related_name = 'blog_unlike')


    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post = models.ForeignKey(Posts,related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    user = models.ForeignKey(R_User, on_delete=models.CASCADE)
    # upvotes = models.IntegerField(default=0)
    # downvotes = models.IntegerField(default=0)
    # score = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return '%s-%s' % (self.post.id,self.user.id)
    

