from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booking-home'),
    path('booking_form/', views.booking_form, name='booking-form'),
]
