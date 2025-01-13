from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Post
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'website/blog.html', context)