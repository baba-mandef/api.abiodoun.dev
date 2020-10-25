from django.shortcuts import render
from henri.blog.models import (Post, Category, Comment, ViewCount)
from henri.blog.forms import CommentForm


def posts(request):
    all_posts = Post.objects.all
    cats = Category.objects.all()

    context = {'posts': all_posts, 'cats': cats}
    return render(request, 'post.html', context)


def details(request, slug):
    post = Post.objects.get(slug=slug)
    cats = Category.objects.all()

    def visitor_ip_address(request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = visitor_ip_address(request)  # get visitor ip
    post_ip = ViewCount.objects.filter(post=post, ip_adress=ip)  # get counter for user ip and post

    if post_ip:
        post.view = post.view
        post.save()
    elif not post_ip:
        new_ip = ViewCount(post=post, ip_adress=ip)
        new_ip.save()
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
