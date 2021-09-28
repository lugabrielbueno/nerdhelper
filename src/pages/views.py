from django.shortcuts import render
from calls.models import Call
from categories.models import Category
from priorities.models import Priority
from nerds.models import Nerd
from django import forms
from django.contrib import messages
# Create your views here.


def home_view(request, *args, **kwargs):

    try:

        context = {
            "categories": Category.objects.all(),
            "priorities": Priority.objects.all(),
            "nerds": Nerd.objects.all()
        }

        if request.method == 'POST':

            Calls = Call()
            Calls.clientCall = request.POST['client']
            Calls.companyCall = request.POST['company']
            Calls.emailResponseCall = request.POST['email']
            Calls.descriptionCall = request.POST['description']
            Calls.solutionCall = request.POST['solution']
            Calls.categoryCall = request.POST['category']
            Calls.priorityCall = request.POST['priority']
            Calls.subjectCall = request.POST['subject']
            Calls.statusCall = 1  # open status
            Calls.nerdCall = request.POST['nerd']

            if not Calls.clientCall:
                raise forms.ValidationError("This field is required")
            if not Calls.companyCall:
                raise forms.ValidationError("This field is required")
            if not Calls.descriptionCall:
                raise forms.ValidationError("This field is required")
            if not Calls.subjectCall:
                raise forms.ValidationError("This field is required")

            Calls.save()
            messages.success(request,"Call registered successfully")
    except forms.ValidationError as val_err:
        messages.warning(request,val_err)

    return render(request, "home.html", context)


def menu_view(request, *args, **kwargs):

    return render(request, "menu.html", {})


def settings_view(request, *args, **kwargs):

    return render(request, "settings/list.html", {})
