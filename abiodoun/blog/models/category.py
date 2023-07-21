from django.db import models
from abiodoun.abstract.models import AbiodounObject


class Category(AbiodounObject):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    def __str__(self):
        return self.title
