from threading import Thread
from django.contrib import admin
from .models import User,Subreddit,Moderator,Threads

# Register your models here.
admin.site.register(User)
admin.site.register(Subreddit)
admin.site.register(Moderator)
admin.site.register(Threads)