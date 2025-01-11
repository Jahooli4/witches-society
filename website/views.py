from django.shortcuts import render
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

# Create your views here.

posts = [
    {
        'author': 'Michelle',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'January 10, 2025',
    },
    {
        'author': 'Catherine',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'January 15, 2025',
    }
]

def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'website/blog.html', context)