from django.urls import path
from henri.blog.views import posts, details, categories

urlpatterns = [
    path('', posts, name='posts'),
    path('post/<slug:slug>', details, name='details'),
    path('category/<str:category>', categories, name='category' )
]
