from django.db import models
from abiodoun.abstract.models import AbiodounObject
from tinymce.models import HTMLField
from .category import Category


class Post(AbiodounObject):
    slug = models.SlugField(max_length=255, unique=True)

    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='blog/post_banner')
    post = HTMLField()

    en_title = models.CharField(max_length=255, blank=True)
    en_banner = models.ImageField(upload_to='blog/post_banner', blank=True)
    en_post = HTMLField(blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    @property
    def post_display(self):
        if '\\U' in self.post or '\\u' in self.post:
            return self.post.encode('utf-8').decode('unicode-escape')
        return self.post
    
    def save(self, *args, **kwargs):
        if '\\U' not in self.post and '\\u' not in self.post:
            self.post = self.post.encode('unicode-escape').decode('utf-8')
        return super().save(*args, **kwargs)
