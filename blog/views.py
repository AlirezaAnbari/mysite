from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')
