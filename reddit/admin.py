from threading import Thread
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(R_User)
admin.site.register(Subreddit)
admin.site.register(Moderator)
admin.site.register(Comment)
admin.site.register(Posts)