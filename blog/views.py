from django.shortcuts import render

from . import models


def blog(request):
    posts = models.Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})


def blog_detail(request, id):
    post = models.Post.objects.get(id=id)
    recent_posts = models.Post.objects.order_by("-created_at")
    context = {
        "recent_posts": recent_posts,
        "post": post
    }
    return render(request, 'blog/blog-detail.html', context)