from django.db import models
from tinymce import HTMLField
from cloudinary.models import CloudinaryField

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=255, unique=True)
    banner= models.ImageField(upload_to='work/work_banner')
    body = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
