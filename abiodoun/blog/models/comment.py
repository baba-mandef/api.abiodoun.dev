from django.db import models
from abiodoun.abstract.models import AbiodounObject
from .post import Post
from pyemoji import encode


class Comment(AbiodounObject):
    body = models.TextField()
    author_name = models.CharField(max_length=50)
    author_mail = models.EmailField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name
    
    def save(self, *args, **kwargs):
        self.body = encode(self.body)
        return super().save()
