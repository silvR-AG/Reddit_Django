from asyncio.proactor_events import _ProactorSocketTransport
from dataclasses import field
from django import forms
from .models import *



class AddPost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'body',
            'author',
            'subreddit',
        ]


class AddSubreddit(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = [
            'name',
            'description',
        ]


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {'body': forms.Textarea(attrs={'rows':4, 'cols':80})}