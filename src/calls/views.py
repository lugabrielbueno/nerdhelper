from django.shortcuts import render
from .models import Call
# Create your views here.
def calls_detail_view(request):

    # calls = Call.objects.get(id=request)
    # context = {
    # "descriptionCall": calls.descriptionCall,
    # "categoryCall": calls.categoryCall,
    # "subjectCall": calls.subjectCall,
    # "clientCall": calls.clientCall,
    # "companyCall": calls.companyCall,
    # "emailResponseCall": calls.emailResponseCall,
    # "status": calls.statusCall
    # }
    return render(request,"calls/detail.html",{})

def calls_list_view(request, *args, **kwargs):
    calls = {
        "calls":  [
                  {"id": 1, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 2, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 14, "category": 3, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 10, "category": 2, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 6, "category": 1, "clientName": "NameClient", "companyName": "nameCompany"},
                  ]
    }
    return render(request, "calls/list.html", calls)

def mycalls_list_view(request, *args, **kwargs):
    mycalls = {
        "mycalls":  [
                  {"id": 1, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 2, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 14, "category": 3, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 10, "category": 2, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 6, "category": 1, "clientName": "NameClient", "companyName": "nameCompany"},
                  ]
    }
    return render(request, "mycalls/list.html", mycalls)

def mycalls_detail_view(request, *args, **kwargs):
    mycalls = {
        "mycalls":  [
                  {"id": 1, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 2, "category": 4, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 14, "category": 3, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 10, "category": 2, "clientName": "NameClient", "companyName": "nameCompany"},
                  {"id": 6, "category": 1, "clientName": "NameClient", "companyName": "nameCompany"},
                  ]
    }
    return render(request, "mycalls/detail.html", mycalls)


def standbycalls_view(request, *args, **kwargs):

    return render(request, "standbycalls.html", {})


def closedcalls_view(request, *args, **kwargs):

    return render(request, "closedcalls.html", {})