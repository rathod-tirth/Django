from django.shortcuts import render
from .models import *

# Create your views here.


def posts_lists(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts_lists.html", {"posts": posts})


def posts_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})
