from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('blog/', PostListView.as_view(), name='website-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='website-about'),
]
