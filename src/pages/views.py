from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):

    return render(request, "home.html",{})



def menu_view(request, *args, **kwargs):

    return render(request, "menu.html", {})
