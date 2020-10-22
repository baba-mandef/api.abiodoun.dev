from django.urls import path
from henri.blog.views import posts

urlpatterns = [
    path('', posts, name='posts'),
]
