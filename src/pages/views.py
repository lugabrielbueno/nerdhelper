from django.shortcuts import render
from calls.models import Call
from categories.models import Category
from priorities.models import Priority
from nerds.models import Nerd
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
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
            if request.POST['nerd']:
                nerd = Nerd.objects.get(id=request.POST['nerd'])    
                Calls.nerdCall = nerd.nerdLogin

            if not Calls.clientCall:
                raise forms.ValidationError("This field is required")
            if not Calls.companyCall:
                raise forms.ValidationError("This field is required")
            if not Calls.descriptionCall:
                raise forms.ValidationError("This field is required")
            if not Calls.subjectCall:
                raise forms.ValidationError("This field is required")

            Calls.save()
            messages.success(request, "Call registered successfully")
    except forms.ValidationError as val_err:
        messages.warning(request, val_err)

    return render(request, "home.html", context)


def menu_view(request, *args, **kwargs):

    return render(request, "menu.html", {})


def settings_view(request, *args, **kwargs):

    return render(request, "settings/list.html", {})


def login_view(request, *args, **kwargs):

    try:
        if request.method == 'POST':

            username = request.POST['username'].lower()

            nerdUser = User.objects.get(username=username)

            passtyped = request.POST['pass']

            user = authenticate(username=nerdUser.username, password=passtyped)
  
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "home.html", {})
            else:
                messages.info(request, "Invalid credentials")

    except Exception as val_err:
        messages.info(request, val_err)
    return render(request, "login.html", {})

def create_user_view(request, *args, **kwargs):

    try:
        if request.method == 'POST':
            nerd = Nerd()
            nerd.nerdName = request.POST['name']
            nerd.nerdLogin = request.POST['username'].lower()
            # nerd.nerdLogin = request.POST['email'].lower()

            loginExists = Call.objects.raw(
                "SELECT id FROM nerds_nerd WHERE nerdName = '"+str(request.POST['name']) + "' ")

            if not loginExists:

                pass_1 = request.POST['pass']
                pass_confirm = request.POST['confirmPass']

                if len(pass_1) < 8:
                    raise Exception(messages.info(
                        request, "This field requires at least 8 characters"))

                if not nerd.nerdName:
                    raise forms.ValidationError(messages.info(
                        request, "This field is required"))
                if not nerd.nerdLogin:
                    raise forms.ValidationError(messages.info(
                        request, "This field is required"))
                if not pass_1:
                    raise forms.ValidationError(messages.info(
                        request, "This field is required"))

                if pass_1 != pass_confirm:
                    raise forms.ValidationError(messages.info(
                        request, "The passwords do not match"))

                nerdUser = User.objects.create_user(
                    username=nerd.nerdLogin, email=request.POST['email'].lower(), password=pass_confirm)
                nerdUser.save()

                nerd.save()
                messages.success(request, "Nerd successfully registered")
                
                user = authenticate(username=nerd.nerdLogin, password=pass_confirm)
             
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, "home.html", {})
                else:
                    messages.info(request, "Invalid credentials")
                
                return render(request, "home.html", {})
            else:
                raise Exception(messages.info(
                    request, "This login already exists"))

    except Exception as val_err:
        messages.error(request, val_err)

    except forms.ValidationError as val_err:
        messages.error(request, val_err)

    return render(request, "new_user.html", {})

    # if check_password(passtyped,nerdUser.password):

    #     return render(request, "home.html", {})


def logout_user_view(request, *args, **kwargs):
    logout(request)
    return render(request, 'login.html', {})
