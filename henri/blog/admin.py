from django.contrib import admin
from henri.blog.models import (Post, Category, Comment, ViewCount)
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

class ViewResource(resources.ModelResource):

    class Meta:
        model = Post


class ViewAdmin(ImportExportModelAdmin):
    resource_class = ViewResource




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ViewCount, ViewAdmin)
