from django.shortcuts import render
from .models import Call
from categories.models import Category
from status.models import Status
from priorities.models import Priority
from nerds.models import Nerd


# Create your views here.

# def formCalls(request,*args,**kwargs):
#     data = {"formCall": CallForm()}
#     return render(request,'calls/create.html', data)


# def calls_create_view(request,*args,**kwargs):

#     return render(request,"calls/create.html",{})

def calls_detail_view(request, id):

    call = Call.objects.get(id=id)

    # nerdName = Nerd.objects.filter(id=call.nerdCall)

    context = {
        "call": call,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        "nerds": Nerd.objects.all()
    }

    return render(request, "calls/detail.html", context)


def calls_list_view(request, *args, **kwargs):
    calls = Call.objects.all()

    # nerdName = Nerd.objects.filter(id=calls.nerdCall)
    context = {
        "calls": calls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        # "nerdName": nerdName
    }

    return render(request, "calls/list.html", context)


# def mycalls_list_view(request, *args, **kwargs):

#     return render(request, "mycalls/list.html", {})


# def mycalls_detail_view(request, *args, **kwargs):

#     return render(request, "mycalls/detail.html", {})





# def closedcalls_view(request, *args, **kwargs):

#     return render(request, "closedcalls.html", {})

