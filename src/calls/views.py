from django.shortcuts import render
from .models import Call
from categories.models import Category
from status.models import Status
from priorities.models import Priority
from nerds.models import Nerd
from django.contrib.auth.models import User

# Create your views here.


def calls_detail_view(request, id):

    call = Call.objects.get(id=id)

    if request.method == 'POST':

        if request.POST['priorityCall']:
            call.priorityCall = request.POST['priorityCall']
        if request.POST['statusCall']:
            call.statusCall = request.POST['statusCall']
        if request.POST['solutionCall']:
            call.solutionCall = request.POST['solutionCall']
        if request.POST['categoryCall']:
            call.categoryCall = request.POST['categoryCall']


        if int(request.POST.get('options')) == 2:
            if request.POST.get('nerdCall',False):
                call.nerdCall = request.POST['nerdCall']


        call.save()

    nerd = Nerd.objects.get(nerdLogin=call.nerdCall)
    context = {
        "call": Call.objects.get(id=id),
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        "nerds": Nerd.objects.all(),
        "nerdSelected": nerd.nerdName
    }

    return render(request, "calls/detail.html", context)


def calls_list_view(request, *args, **kwargs):
    # nerd = request.user.username

    calls = Call.objects.all()

    context = {
        "calls": calls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        # "nerdName": nerdName
        }

    return render(request, "calls/list.html", context)


def mycalls_detail_view(request, id):
    mycall = Call.objects.get(id=id)

    if request.method == 'POST':

        if request.POST['priorityCall']:
            mycall.priorityCall = request.POST['priorityCall']
        if request.POST['statusCall']:
            mycall.statusCall = request.POST['statusCall']
        if request.POST['solutionCall']:
            mycall.solutionCall = request.POST['solutionCall']
        if request.POST['categoryCall']:
            mycall.categoryCall = request.POST['categoryCall']


        if int(request.POST.get('options')) == 2:
            if request.POST.get('nerdCall',False):
                mycall.nerdCall = request.POST['nerdCall']


        mycall.save()

    nerd = Nerd.objects.get(nerdLogin=mycall.nerdCall)
    context = {
        "mycall": Call.objects.get(id=id),
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        "nerds": Nerd.objects.all(),
        "nerdSelected": nerd.nerdName
    }


    return render(request, "mycalls/detail.html", context)


def mycalls_list_view(request, *args, **kwargs):
    nerd = request.user.username

    mycalls = Call.objects.filter(nerdCall=nerd)

    context = {
        "mycalls": mycalls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        # "nerdName": nerdName
        }

    return render(request, "mycalls/list.html", context)

def calls_list_search_view(request, *args, **kwargs):
    # nerd = request.user.username


    calls = Call.objects.all()
    if request.method == 'GET':
        status = request.GET.get('statusCall')
        prior = request.GET.get('priorityCall')
        categ = request.GET.get('categoryCall')


        if int(status) != 0:
            calls.filter(statusCall=status)

        if int(prior) != 0:
            calls.filter(priorityCall=prior)

        if int(categ) != 0:
            calls.filter(categoryCall=categ)
 


        context = {
        "calls": calls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        # "nerdName": nerdName
        }



    return render(request, "calls/list.html", context)




def mycalls_list_search_view(request, *args, **kwargs):
    nerd = request.user.username

    mycalls = Call.objects.filter(nerdCall=nerd)

    context = {
        "mycalls": mycalls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),
        # "nerdName": nerdName
        }

    if request.method == 'GET':
        status = request.GET.get('statusCall')
        prior = request.GET.get('priorityCall')
        categ = request.GET.get('categoryCall')



        if int(status) != 0:
            context['status'] = Status.objects.filter(id=status)


        if int(prior) != 0:
            context['priorities'] = Priority.objects.filter(id=prior)


        if int(categ) != 0:
            context['categories'] = Category.objects.filter(id=categ)





    return render(request, "mycalls/list.html", context)

# def closedcalls_view(request, *args, **kwargs):

#     return render(request, "closedcalls.html", {})

