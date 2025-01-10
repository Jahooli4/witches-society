from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('blog/', views.blog, name='website-blog'),
]
