from django.shortcuts import render
from henri.blog.models import Post, Category, Comment


def posts(request):
    all_posts = Post.objects.all
    cats = Category.objects.all()

    context = {'posts': all_posts, 'cats': cats}
    return render(request, 'post.html', context)


def details(request, slug):
    post = Post.objects.get(slug=slug)
    cats = Category.objects.all()
    post.view += 1
    post.save()
    comments = Comment.objects.filter(id=post.id)
    context = {'post': post, 'cats': cats, 'comments': comments}
    return render(request, 'post-details.html', context)
