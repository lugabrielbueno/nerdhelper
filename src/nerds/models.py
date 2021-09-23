from django.db import models

# Create your models here.
class Nerd(models.Model):
    nerdName = models.CharField(max_length=120,null=False,blank=False)
    