from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50,null=False,blank=False)