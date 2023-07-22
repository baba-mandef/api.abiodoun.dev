from django.db import models
from tinymce.models import HTMLField
from abiodoun.abstract.models import AbiodounObject


class Work(AbiodounObject):
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    en_description = models.CharField(max_length=500, blank=True)
    banner= models.ImageField(upload_to='work/work_banner')
    body = HTMLField()
    en_body = HTMLField(blank=True)
    stack = models.CharField(max_length=255)
    link = models.CharField(max_length=500)
    repo = models.CharField(max_length=500)



    def __str__(self):
        return self.name
