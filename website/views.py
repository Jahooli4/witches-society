from django.shortcuts import render
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def blog(request):
    return render(request, 'website/blog.html')