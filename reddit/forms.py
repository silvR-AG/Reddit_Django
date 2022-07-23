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
            'img',
            'subreddit',
        ]
    widgets = {
        'title' : forms.Textarea(attrs={'rows': 1,'class':'form-control'}),
        'body' : forms.Textarea(attrs={'cols':80 ,'class':'form-control'}),

    }

class AddSubreddit(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.Textarea(attrs={'rows': 1,'class':'form-control'}),
            'description': forms.Textarea(attrs={'cols':80 ,'class':'form-control'}),
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            # 'post',
            # 'user',
            'body',
        ]
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'user': forms.Textarea(attrs={'rows':1, 'cols':80, 'class':'form-control'})
            }

