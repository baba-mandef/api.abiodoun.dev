from rest_framework.serializers import ModelSerializer
from abiodoun.blog.models import (Post, Comment, Category)
import base64


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'banner', 'post',
                  'en_title', 'en_banner', 'en_post',
                  'created_at', 'updated_at', 'category',
                  'published',]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'author_name', 'author_mail', 'post', 'created_at']

    def get_body(self, obj):
        return base64.b64decode(obj.body.encode('ascii')).decode('utf-8')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
