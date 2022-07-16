from asyncio.proactor_events import _ProactorSocketTransport
from django import forms
from .models import *



class AddPost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'body',
        ]


class AddSubreddit(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = [
            'name',
            'description',
        ]
