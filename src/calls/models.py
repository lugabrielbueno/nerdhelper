from django.db import models

# Create your models here.


class Call(models.Model):
    descriptionCall = models.TextField(null=False,blank=False)
    categoryCall = models.IntegerField(null=False,blank=False)
    subjectCall = models.CharField(max_length=60,null=False,blank=False)
    clientCall = models.CharField(max_length=30,null=False,blank=False)
    companyCall = models.CharField(null=False,blank=False,max_length=30)
    priorityCall = models.IntegerField(null=False,blank=False,default=0)
    emailResponseCall = models.EmailField(null=False,blank=False)
    statusCall = models.IntegerField(default=0,null=False,blank=False)
    solutionCall = models.TextField(default='',null=False,blank=False)
    nerdCall = models.IntegerField(default=0)