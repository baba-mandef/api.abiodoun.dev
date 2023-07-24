from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class AbiodounObjectManager(models.Manager):

    def get_by_id(self, id, **kwargs):
        
        error_message = "{self.model.__name__} does not exist"

        if id == "undefined":
            raise ObjectDoesNotExist(error_message)
        qs = self.filter(**kwargs)

        try:
            instance = qs.get(id=id)
        except (ObjectDoesNotExist, ValidationError, TypeError, ValueError) as e:
            raise ObjectDoesNotExist(error_message)
        return instance


class AbiodounObject(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AbiodounObjectManager()
    
    class Meta:
        abstract = True
