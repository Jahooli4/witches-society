from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('blog/', views.blog, name='website-blog'),
    path('about/', views.about, name='website-about'),
]
