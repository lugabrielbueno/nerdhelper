from django.shortcuts import redirect, render
from .models import Category
from django import forms
from django.contrib import messages

# Create your views here.
def categories_list_view(request,*args,**kwargs):

    categories = {"categories": Category.objects.all() }

    return render(request,'categories/list.html',categories)


def categories_create_view(request,*args,**kwargs):

    if request.method == 'POST':

        Categ = Category()
        Categ.categoryName = request.POST['categoryName']

        if not Categ.categoryName:
            raise forms.ValidationError("This field is required")

        Categ.save()

        categories = {"categories": Category.objects.all() }

    return render(request,'categories/list.html',categories)


def categories_update_view(request,*args,**kwargs):

    if request.method == 'POST':


        Categ = Category.objects.get(id=request.POST['categoryId'])
        Categ.categoryName = request.POST['categoryName']

        Categ.save()

        categories = {"categories": Category.objects.all() }

        messages.success(request, 'Successfully updated')

    return render(request,'categories/list.html',categories)


def categories_delete_view(request,id,*args,**kwargs):

    if request.method == 'POST':

        Categ =  Category.objects.get(id=request.POST['categoryId'])
        Categ.delete()

        messages.success(request, 'Successfully deleted')

        categories = {"categories": Category.objects.all() }
        
        return render(request,'categories/list.html',categories)

    else:
    
        cat =  {"cat": Category.objects.get(id=id) }


        return render(request,'categories/category_delete.html',cat)