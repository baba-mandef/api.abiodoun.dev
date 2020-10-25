from django.contrib import admin
from henri.blog.models import (Post, Category, Comment, ViewCount)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ViewCount)
