from rest_framework.routers import DefaultRouter
from abiodoun.blog.viewsets import (PostViewSet, CategoryViewSet, CommentViewSet)
from abiodoun.work.viewsets import WorkViewset
from abiodoun.message.viewsets import MessageViewSet
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)

router.register(r'blog/post', PostViewSet, basename='post')
router.register(r'blog/category', CategoryViewSet, basename='category')
router.register(r'blog/comment', CommentViewSet, basename='comment')
router.register(r'message/new', MessageViewSet, basename='message')
# router.register(r'blog/view', ViewViewSet, basename='view')
router.register(r'work', WorkViewset, basename='work')


urlpatterns = [
    # path('getIp/', GetUserIP.as_view()),
    # path('countView/', ViewCounter.as_view()),
    path('', include(router.urls)),
   
]
