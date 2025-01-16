from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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

class PostListView(ListView):
    model = Post
    template_name = 'website/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)