from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from henri.blog.serializers import PostSerializer, CommentSerializer, ViewSerializer, CategorySerializer
from henri.blog.models import Comment, Category, ViewCount, Post


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_pk = self.request.query_params['post']
        if post_pk is not None:
            queryset = Comment.objects.filter(post=post_pk)
        return queryset



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']


class ViewViewSet(ModelViewSet):
    serializer_class = ViewSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        post_pk = self.request.query_params['post']
        return ViewCount.objects.filter(post=post_pk)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        slug = self.request.query_params.get('slug')
        if slug is not None:
            queryset = Post.objects.filter(slug=slug)
        return queryset

