from django.db import models


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    des = models.CharField(max_length=20)

    def __str__(self):
        return self.des


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
