import email
from enum import Flag
from pickle import FALSE, TRUE
from django.contrib.auth.models import User
from email import message
from django.urls import resolve
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.template import TemplateSyntaxError
from django.urls import reverse_lazy, reverse
from requests import post
from django.views.generic import DetailView, CreateView
# Create your views here.
from .models import *
from .forms import *


def home(request):
    obj = Posts.objects.all().order_by('-date_created')
    # print(str(obj.query),'\n\n\n')
    objsub = Subreddit.objects.all()
    # print(obj.values())
    context = {
        'data': obj.values(), 'sub' : objsub.values()
    }

    return render(request, 'reddit/index.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        c_pwd = request.POST.get('c_pwd')

        if R_User.objects.filter(username=username):
            messages.error(request, "Username not available")
            return redirect(register)
        if R_User.objects.filter(email=email):
            messages.error(request, "E-mail already in use.")
            return redirect(register)
        if pwd != c_pwd:
            messages.error(request, "Password does not match")
            return redirect(register)

        myuser = R_User.objects.create_user(username, email, pwd)

        myuser.save()
        messages.success(request, "User Registered Successfully")

        return redirect('/login')
    return render(request, 'reddit/register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        user = authenticate(username=username, password=pwd)

        if user is not None:
            login(request, user)
            return render(request, "reddit/index.html", {'username': username})
        else:
            messages.error(request, "Invalid login")
            return redirect(home)
    return render(request, 'reddit/login.html')


def Logout(request):
    logout(request)
    # messages.success(request,"Logged out successfully")
    return redirect(home)


def addpost(request):
    if request.method == 'POST':
        form = AddPost(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            # messages.success(request,"Posted successfully")
            return redirect(home)
    else:
        form = AddPost()
    return render(request, 'reddit/addpost.html', {'form': form})


def addsubreddit(request):
    if request.method == 'POST':
        form = AddSubreddit(request.POST)
        if form.is_valid():
            form.save()
            return redirect(subred)
    else:
        form = AddSubreddit()
    return render(request, 'reddit/addsubreddit.html', {'form': form})


def addcomment(request, id):

    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = AddComment()

    def form_valid(self, form):
        form.instance.post = self.kawrgs['id']
        return super().form_valid(form)
    return render(request, 'reddit/addcomment.html', {'form': form})


def postdetail(request, id):
    pst = get_object_or_404(Posts, pk=id)
    user_obj = R_User.objects.all()
    totallikes = pst.total_likes()
    totalunlikes = pst.total_unlikes()
    score = totallikes - totalunlikes
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.post = pst
            obj.user = request.user
            obj.save()
            return redirect("PostDetail", id = pst.id)
    else:
        form = AddComment()

    # sub = get_object_or_404(Subreddit, pk = id)
    template = 'reddit/post.html'
    context = {'post': pst, 'total':score, 'form':form}

    return render(request, template, context)
    # model = Posts
    # template = 'reddit/post.html'


def subred(request, id):
    sub = get_object_or_404(Subreddit, pk=id)
    user_obj = R_User.objects.all()
    post = Posts.objects.all()
    # print(str(post.query),'\n\n\n')

    template = 'reddit/subreddit.html'
    context = {'sub': sub, 'data':post}
    # print (post[0].__dict__, '\n\n')

    return render(request, template, context)



def like_post(request, id):
    post = get_object_or_404(Posts, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('PostDetail', args=[str(id)]))




def unlike_post(request, id):
    post = get_object_or_404(Posts, id = request.POST.get('post_id'))
    liked = False
    if post.unlikes.filter(id = request.user.id).exists():
        post.unlikes.remove(request.user)
        liked = False
    else:
        post.unlikes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('PostDetail', args=[str(id)]))

