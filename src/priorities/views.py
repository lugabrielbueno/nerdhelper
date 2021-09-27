from django.shortcuts import redirect, render
from .models import Priority
from django import forms
from django.contrib import messages

# Create your views here.
def priorities_list_view(request,*args,**kwargs):

    priorities = {"priorities": Priority.objects.all() }

    return render(request,'priorities/list.html',priorities)


def priorities_create_view(request,*args,**kwargs):

    if request.method == 'POST':

        Prior = Priority()
        Prior.priorityName = request.POST['priorityName']

        if not Prior.priorityName:
            raise forms.ValidationError("This field is required")

        Prior.save()

        priorities = {"priorities": Priority.objects.all() }

    return render(request,'priorities/list.html',priorities)


def priorities_update_view(request,*args,**kwargs):

    if request.method == 'POST':


        Prior = Priority.objects.get(id=request.POST['priorityId'])
        Prior.priorityName = request.POST['priorityName']

        Prior.save()

        priorities = {"priorities": Priority.objects.all() }

        messages.success(request, 'Successfully updated')

    return render(request,'priorities/list.html',priorities)


def priorities_delete_view(request,id,*args,**kwargs):

    if request.method == 'POST':

        Prior =  Priority.objects.get(id=request.POST['priorityId'])
        Prior.delete()

        messages.success(request, 'Successfully deleted')

        priorities = {"priorities": Priority.objects.all() }
        
        return render(request,'priorities/list.html',priorities)

    else:
    
        prior =  {"prior": Priority.objects.get(id=id) }


        return render(request,'priorities/priority_delete.html',prior)