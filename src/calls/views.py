from django.shortcuts import render
from .models import Call
from calls.forms import CallForm

# Create your views here.

def formCalls(request,*args,**kwargs):
    data = {"formCall": CallForm()}
    return render(request,'calls/create.html', data)


# def calls_create_view(request,*args,**kwargs):

#     return render(request,"calls/create.html",{})

# def calls_detail_view(request):
#     context = {
#         "call": Call.objects.filter(id=request.id)
#     }

#     return render(request, "calls/detail.html", context)


# def calls_list_view(request, *args, **kwargs):

#     context = {
#         "calls": Call.objects.filter(statusCall=1)
#     }

#     return render(request, "calls/list.html", context)


# def mycalls_list_view(request, *args, **kwargs):

#     return render(request, "mycalls/list.html", {})


# def mycalls_detail_view(request, *args, **kwargs):

#     return render(request, "mycalls/detail.html", {})





# def closedcalls_view(request, *args, **kwargs):

#     return render(request, "closedcalls.html", {})

