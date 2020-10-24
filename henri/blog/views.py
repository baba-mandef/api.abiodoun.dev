from django.shortcuts import render
from henri.blog.models import (Post, Category, Comment)
from henri.blog.forms import CommentForm


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
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    comments = Comment.objects.filter(post=post.id)
    context = {'post': post, 'cats': cats, 'comments': comments, 'form': form}
    return render(request, 'post-details.html', context)


def categories(request, category):
    posts = Post.objects.filter(category__title=category)
    cats = Category.objects.all()
    cat_title = category

    context = {'posts': posts, 'cats': cats, 'cat_title': cat_title}
    return render(request, 'category.html', context)
