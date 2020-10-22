from django.shortcuts import render
from henri.blog.models import Post, Category


def posts(request):
    all_posts = Post.objects.all
    cats = Category.objects.all()

    context = {'posts': all_posts, 'cats': cats}
    return render(request, 'post.html', context)
