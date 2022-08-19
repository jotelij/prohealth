from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Institution(BaseModel):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
