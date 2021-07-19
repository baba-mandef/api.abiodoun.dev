from django.shortcuts import render
from henri.blog.models import (Post, Category, Comment, ViewCount)
from henri.blog.forms import CommentForm
from henri.utils.get_ip import visitor_ip_address
from telegram.ext import (Updater, CallbackContext)
from root.settings import token, chat
from henri.utils.check_comment import checking

update = Updater(token, use_context=True)
job = update.job_queue


def posts(request):
    """
    list all available posts
    :param request:
    :return context:
    """
    all_posts = Post.objects.filter(published=True)
    cats = Category.objects.all()

    context = {'posts': all_posts, 'cats': cats}
    return render(request, 'post.html', context)


def details(request, slug):
    """
    Return details for a specific post
    :param request:
    :param slug:
    :return context:
    """
    post = Post.objects.get(slug=slug)  # Get post
    cats = Category.objects.all()  # get all posts categories

    ip = visitor_ip_address(request)  # get visitor ip
    post_ip = ViewCount.objects.filter(post=post, ip_adress=ip)  # get view object for user_ip and post
    def callback_view(context: CallbackContext):
        context.bot.send_message(chat_id=chat,
                                text=' Reader ip : {}\n Post title : {} \n First time : True \n link : https://henri-dev.tech/blog/post/{}'.format(ip, post.title, post.slug))
    def callback_review(context: CallbackContext):
        context.bot.send_message(chat_id=chat,
                                text=' Reader ip : {}\n Post title : {} \n First time : False \n link : https://henri-dev.tech/blog/post/{}'.format(ip, post.title, post.slug))

    def callback_comment(context: CallbackContext):
        context.bot.send_message(chat_id=chat,
                                text=' Comment author ip : {} \n\n Comment body : \n {} \n\n Post title : {} \n link : https://henri-dev.tech/blog/post/{}'.format(ip, comment.body, post.title, post.slug))

    if post_ip:
        # check if the visitor has already read this post
        post.view = post.view
        job.run_once(callback_review, 1)

        post.save()

    elif not post_ip and post.published:
        # check if the visitor has not read this post and if post is already published
        # add new view for the post
        new_ip = ViewCount(post=post, ip_adress=ip)
        new_ip.save()
        post.view += 1
        job.run_once(callback_view, 1)

        post.save()



    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(data=request.POST)  # get form data
        if form.is_valid():
            # check form validity and save comment
            comment = form.save(commit=False)
            body = comment.body
            check=checking(body)
            if check:
                form.save(commit=False)
            else:
                comment = form.save(commit=False)
                comment.post = post
                job.run_once(callback_comment, 1)
                comment.save()

    comments = Comment.objects.filter(post=post.id)  # get all comment for the post
    context = {'post': post, 'cats': cats, 'comments': comments, 'form': form}
    update.start_polling()
    return render(request, 'post-details.html', context)


def categories(request, category):
    """
    list all available posts by category
    :param request:
    :param category:
    :return:
    """
    posts = Post.objects.filter(category__title=category, published=True)
    cats = Category.objects.all()
    cat_title = category

    context = {'posts': posts, 'cats': cats, 'cat_title': cat_title}
    return render(request, 'category.html', context)
