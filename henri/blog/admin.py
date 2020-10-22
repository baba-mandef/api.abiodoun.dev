from django.contrib import admin
from henri.blog.models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
