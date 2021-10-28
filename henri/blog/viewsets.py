from rest_framework.viewsets import ModelViewSet
from henri.blog.serializers import PostSerializer, CommentSerializer, ViewSerializer, CategorySerializer
from henri.blog.models import Comment


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        post_pk = self.kwargs['post_id']

        return Comment.objects.filter(post=post_pk)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ['get']


class ViewViewSet(ModelViewSet):
    serializer_class = ViewSerializer
    http_method_names = ['get', 'post']


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put']
