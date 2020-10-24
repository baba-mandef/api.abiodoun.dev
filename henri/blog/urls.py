from django.urls import path
from henri.blog.views import posts, details

urlpatterns = [
    path('', posts, name='posts'),
    path('post/<slug:slug>', details, name='details')
]
