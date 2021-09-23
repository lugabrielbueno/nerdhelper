from django.db import models

# Create your models here.


class Call(models.Model):
    descriptionCall = models.TextField(null=False,blank=False)
    categoryCall = models.IntegerField(null=False,blank=False)
    subjectCall = models.CharField(max_length=60,null=False,blank=False)
    clientCall = models.TextField(max_length=30,null=False,blank=False)
    companyCall = models.TextField(null=False,blank=False,max_length=30)
    emailResponseCall = models.EmailField(null=False,blank=False)
    status = models.IntegerField(default=0,null=False,blank=False)