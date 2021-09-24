from django.shortcuts import render
from calls.models import Call
from categories.models import Category
from priorities.models import Priority
# Create your views here.


def home_view(request, *args, **kwargs):

    context = {
        "categories": Category.objects.all(),
        "priorities": Priority.objects.all()
    }

    if request.method == 'POST':

        Calls = Call()
        Calls.clientCall = request.POST.get('client')
        Calls.companyCall = request.POST.get('company')
        Calls.emailResponseCall = request.POST.get('email')
        Calls.descriptionCall = request.POST.get('description')
        Calls.solutionCall = request.POST.get('solution')
        Calls.categoryCall = request.POST.get('category')
        Calls.priorityCall = request.POST.get('priority')
        Calls.subjectCall = request.POST.get('subject')
        Calls.statusCall = 1 # open status
        Calls.nerdCall = 0 # open status
        Calls.save()

    return render(request, "home.html", context)


def menu_view(request, *args, **kwargs):

    return render(request, "menu.html", {})


def settings(request, *args, **kwargs):

    return render(request, "settings.html", {})
