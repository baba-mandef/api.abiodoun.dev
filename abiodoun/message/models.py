from django.db import models
from abiodoun.abstract.models import AbiodounObject


class Message(AbiodounObject):
    sender_name = models.CharField(max_length=150)
    sender_email = models.EmailField()
    body = models.TextField()
