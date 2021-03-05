from django.shortcuts import render
from .models import Post





# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'djblogapp/index.html', {'posts': posts})

def about(request):
    return render(request, 'djblogapp/about.html')


