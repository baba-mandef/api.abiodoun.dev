from rest_framework.views import APIView
from henri.utils.get_ip import visitor_ip_address
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from telegram.ext import (Updater, CallbackContext)
from root.settings import token, chat
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from django.shortcuts import get_object_or_404
from henri.blog.serializers import PostSerializer, CommentSerializer, ViewSerializer, CategorySerializer
from henri.blog.models import Comment, Category, ViewCount, Post

update = Updater(token, use_context=True)
job = update.job_queue


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_pk = self.request.query_params.get('post')
        if post_pk is not None:
            queryset = Comment.objects.filter(post=post_pk)
        return queryset



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']


""" class ViewViewSet(ModelViewSet):
    serializer_class = ViewSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        post_pk = self.request.query_params.get('post')
        return ViewCount.objects.filter(post=post_pk) """


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        slug = self.request.query_params.get('slug')
        if slug is not None:
            queryset = Post.objects.filter(slug=slug)
        return queryset


class GetUserIP(APIView):

    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return Response(ip)


class ViewCounter(APIView):

    def get(self, request):
        ip = visitor_ip_address(request)
        post_pk = request.query_params.get('post')
        post = Post.objects.get(pk=post_pk)
        view = ViewCount.objects.filter(post=post_pk, ip_adress=ip)

        def callback_view(context: CallbackContext):
            context.bot.send_message(chat_id=chat,
                                     text=' Reader ip : {}\n Post title : {} \n First time : True \n link : https://henri-dev.tech/blog/post/{} \n views : {}'.format(
                                         ip, post.title, post.slug, post.view))

        def callback_review(context: CallbackContext):
            context.bot.send_message(chat_id=chat,
                                     text=' Reader ip : {}\n Post title : {} \n First time : False \n link : https://henri-dev.tech/blog/post/{} \n views : {}'.format(
                                         ip, post.title, post.slug, post.view))
        if view and post.published:
            post.view = post.view
            post.save()
            job.run_once(callback_review, 1)
            return Response("Already read")
        elif not view and post.published:
            post.view = post.view + 1
            new_ip = ViewCount(post=post, ip_adress=ip)
            new_ip.save()
            job.run_once(callback_view, 1)
            post.save()
            return Response("New reader")





