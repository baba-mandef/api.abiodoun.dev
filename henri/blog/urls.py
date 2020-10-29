from django.urls import path
from henri.blog.views import (posts, details, categories)

urlpatterns = [
    path('', posts, name='posts'),  # all posts route
    path('post/<slug:slug>', details, name='details'),  # post details route
    path('category/<str:category>', categories, name='category'),  # all posts by category route
]
