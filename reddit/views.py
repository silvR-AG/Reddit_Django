from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.
from .models import *


def index(request):
    return render(request, 'reddit/index.html')

def registerpage(request):
    form = UserCreationForm()
    context  = {'form': form}