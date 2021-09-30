from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Nerd
from calls.models import Call
from nerds.models import Nerd
from django import forms
from django.contrib import messages
import bcrypt
from django.contrib.auth.models import User


# Create your views here.


def nerd_list_view(request, *args, **kwargs):

    context = {
        "nerds": Nerd.objects.all()
    }
    return render(request, 'nerds/list.html', context)


def nerd_detail_view(request, id, *args, **kwargs):

    qttByCateg = Call.objects.raw(
        "SELECT COUNT(id) as quantity FROM calls_call WHERE nerdCall = '"+str(id) + "' GROUP BY categoryCall ").columns

    context = {
        "nerd": Nerd.objects.get(id=id),
        "solveds": qttByCateg
    }
    return render(request, 'nerds/detail.html', context)


def nerd_create_view(request, *args, **kwargs):

    try:
        if request.method == 'POST':
            nerd = Nerd()
            nerd.nerdName = request.POST['nerdName']
            nerd.nerdLogin = request.POST['nerdLogin'].lower()

            loginExists = Call.objects.raw(
                "SELECT id FROM nerds_nerd WHERE nerdName = '"+str(request.POST['nerdName']) + "' ")

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
                nerdUser = User.objects.create_user(nerd.nerdLogin, 'teste@gmsail.com', pass_confirm)
                nerdUser.save()



                nerd.save()
                messages.success(request, "Nerd successfully registered")
            else:
                raise Exception("This login alredy exists")

    except Exception as val_err:
        messages.error(request, val_err)
        
    except ValidationError as val_err:
        messages.error(request, val_err)
        

    context = {
        "nerds": Nerd.objects.all()
    }
    return render(request, "nerds/list.html", context)


def nerd_delete_view(request, id, *args, **kwargs):

    if request.method == 'POST':

        Ner = Nerd.objects.get(id=request.POST['nerdId'])
        nerdUser = User.objects.get(username=Ner.nerdLogin)

        nerdUser.delete()
        Ner.delete()

        messages.success(request, 'Successfully deleted')

        nerds = {"nerds": Nerd.objects.all()}

        return render(request, 'nerds/list.html', nerds)

    else:
        nerds = {"nerd": Nerd.objects.get(id=id)}

        return render(request, 'nerds/nerd_delete.html', nerds)
