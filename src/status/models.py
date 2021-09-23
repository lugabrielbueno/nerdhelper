from django.db import models

# Create your models here.
class Status(models.Model):
    statusName = models.CharField(max_length=100,null=False,blank=False)