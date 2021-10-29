from rest_framework.routers import DefaultRouter
from henri.blog.viewsets import (PostViewSet, CategoryViewSet, ViewViewSet, CommentViewSet)
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)

router.register(r'blog/post', PostViewSet, basename='post')
router.register(r'blog/category', CategoryViewSet, basename='category')
router.register(r'blog/comment', CommentViewSet, basename='comment')
router.register(r'blog/view', ViewViewSet, basename='view')


urlpatterns = [
    path('', include(router.urls)),
]
