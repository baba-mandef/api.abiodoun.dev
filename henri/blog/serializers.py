from rest_framework.serializers import ModelSerializer
from henri.blog.models import (Post, Comment, Category, ViewCount)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        field = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        field = '__all__'


class CategorySerializer(ModelSerializer):
    class  Meta:
        model = Category
        field = '__all__'


class ViewSerializer(ModelSerializer):
    class Meta:
        model = ViewCount
        field='__all__'
