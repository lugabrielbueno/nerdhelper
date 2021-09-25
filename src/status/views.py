from django.shortcuts import render
from .models import Status

# Create your views here.

def status_list_view(request,*args,**kwargs):
    status = {"status": Status.objects.all()}
    return render(request,"status.html",status)