from rest_framework.serializers import ModelSerializer
from henri.blog.models import (Post, Comment, Category, ViewCount)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'banner', 'post', 'created_at', 'updated_at', 'category', 'published', 'view']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'body', 'author_name', 'author_mail', 'author_pic', 'post']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ViewSerializer(ModelSerializer):
    class Meta:
        model = ViewCount
        fields = ['id', 'ip_adress', 'post']

