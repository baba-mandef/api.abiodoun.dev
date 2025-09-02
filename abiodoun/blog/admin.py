from django.contrib import admin
from abiodoun.blog.models import (Post, Category, Comment)
from import_export.admin import ImportExportModelAdmin
from import_export import resources
import base64


""" class PostResource(resources.ModelResource):

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
    resource_class = CommentResource """



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "decoded_body", "post", "created_at")
    search_fields = ("author_name", "author_mail", "body")

    def decoded_body(self, obj):
        return obj.body.encode('utf-8').decode('unicode-escape')

    decoded_body.short_description = "Commentaire"



admin.site.register(Post)
admin.site.register(Category)
