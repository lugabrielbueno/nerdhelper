from django.shortcuts import render
from .models import Nerd
from calls.models import Call
from categories.models import Category

# Create your views here.


def nerd_list_view(request, *args, **kwargs):


    context = {
        "nerds": Nerd.objects.all()
    }
    return render(request, 'nerds/list.html', context)


def nerd_detail_view(request,id, *args, **kwargs):


    qttByCateg = Call.objects.raw("SELECT COUNT(id) as quantity FROM calls_call WHERE nerdCall = '"+str(id) + "' GROUP BY categoryCall ").columns

    print(qttByCateg)

    context = {
        "nerd": Nerd.objects.get(id=id),
        "solveds": qttByCateg
    }
    return render(request, 'nerds/detail.html', context)
