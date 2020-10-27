from django.db import models
from tinymce import HTMLField


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    banner = models.ImageField(upload_to='blog/post_banner')
    post = HTMLField('Post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    view = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class ViewCount(models.Model):
    id = models.AutoField(primary_key=True)
    ip_adress = models.GenericIPAddressField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.ip_adress, self.post)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author_name = models.CharField(max_length=50)
    author_mail = models.CharField(max_length=50)
    author_pic = models.ImageField(default='comments/d.png')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name
