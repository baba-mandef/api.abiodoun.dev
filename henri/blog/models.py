from django.db import models
from tinymce import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='blog/post_banner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
