from django.db import models

# Create your models here.
class Priority(models.Model):
    priorityName = models.CharField(max_length=30,null=False,blank=False)