from django.contrib import postgres
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.




class Content(models.Model):
    name = models.CharField(max_length=40)
    data = JSONField()
