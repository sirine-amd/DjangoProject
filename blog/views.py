from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Post

def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    # Récupérer l'article correspondant au slug
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post_detail.html', {'post': post})