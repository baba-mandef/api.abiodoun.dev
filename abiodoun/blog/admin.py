from django.contrib import admin
from abiodoun.blog.models import (Post, Category, Comment)
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PostResource(resources.ModelResource):

    class Meta:
        model = Post
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

class CResource(resources.ModelResource):

    class Meta:
        model = Category

class CAdmin(ImportExportModelAdmin):
    resource_class = CResource

class CommentResource(resources.ModelResource):

    class Meta:
        model = Comment

class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CAdmin)
admin.site.register(Comment, CommentAdmin)
