from django.shortcuts import render
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'booking/home.html')

def booking_form(request):
    return render(request, 'booking/booking_form.html')