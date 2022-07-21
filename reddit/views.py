import email
from email import message
from multiprocessing import context
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.template import TemplateSyntaxError
from django.views.generic import DetailView
# Create your views here.
from .models import *
from .forms import *




def home(request):
    obj = Posts.objects.all()
    print(obj.values())
    context={
        'data': obj,
    }

    return render(request, 'reddit/index.html',context)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        c_pwd = request.POST.get('c_pwd')

        if R_User.objects.filter(username=username):
            messages.error(request,"Username not available")
            return redirect(register)
        if R_User.objects.filter(email=email):
            messages.error(request,"E-mail already in use.")
            return redirect(register)
        if pwd != c_pwd:
            messages.error(request,"Password does not match")
            return redirect(register)

        myuser = R_User.objects.create_user(username, email, pwd)

        myuser.save()
        messages.success(request, "User Registered Successfully")

        return redirect('/login')
    return render(request,'reddit/register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        user = authenticate(username = username,password = pwd)

        if user is not None:
            login(request, user)
            return render(request, "reddit/index.html", {'username': username})
        else:
            messages.error(request,"Invalid login")
            return redirect(home)
    return render(request,'reddit/login.html')

def Logout(request):
    logout(request)
    # messages.success(request,"Logged out successfully")
    return redirect(home)

def addpost(request):
    if request.method ==  'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,"Posted successfully")
            return redirect(home)
    else:
        form = AddPost()
    return render(request, 'reddit/addpost.html', {'form':form})

def addsubreddit(request):
    if request.method ==  'POST':
        form = AddSubreddit(request.POST)
        if form.is_valid():
            form.save()
            return redirect(subred)
    else:
        form = AddSubreddit()
    return render(request, 'reddit/addsubreddit.html', {'form':form})

def addcomment(request):
    if request.method ==  'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect(postdetail)
    else:
        form = AddComment()
    return render(request, 'reddit/addcomment.html', {'form':form})


def postdetail(request,id):
    pst = get_object_or_404(Posts,pk = id)
    # sub = get_object_or_404(Subreddit, pk = id)
    template = 'reddit/post.html'
    context = {'post':pst}
    return render(request,template,context)
    # model = Posts
    # template = 'reddit/post.html'


def subred(request):

    return render(request,'reddit/subreddit.html')