from django.shortcuts import render
from .models import Call
from categories.models import Category
from status.models import Status
from priorities.models import Priority
from nerds.models import Nerd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Config server to send the email with response
host = '<HOST_URL>'
port = 587
user = '<USER>'
password = '<PASS>'



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


        if call.emailResponseCall:
            # the object
            server = smtplib.SMTP(host, port)
            # Login server
            server.ehlo()
            server.starttls()
            server.login(user, password)

            # Creating the message
            message = 'Hello, world!'

            email_msg = MIMEMultipart()
            email_msg['From'] = user
            email_msg['To'] = '<EMAIL_DE_DESTINO>'
            email_msg['Subject'] = 'message subj'
            email_msg.attach(MIMEText(message, 'plain'))

            # Sending the message
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()

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

        if mycall.emailResponseCall:
            # the object
            server = smtplib.SMTP(host, port)
            # Login server
            server.ehlo()
            server.starttls()
            server.login(user, password)

            # Creating the message
            message = 'Hello, world!'

            email_msg = MIMEMultipart()
            email_msg['From'] = user
            email_msg['To'] = '<EMAIL_DE_DESTINO>'
            email_msg['Subject'] = 'message subj'
            email_msg.attach(MIMEText(message, 'plain'))

            # Sending the message
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()

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

    calls = Call.objects.all()
    if request.method == 'GET':
        status = request.GET.get('statusCall')
        prior = request.GET.get('priorityCall')
        categ = request.GET.get('categoryCall')


        if int(status) != 0:
            calls = calls.filter(statusCall=status)

        if int(prior) != 0:
            calls = calls.filter(priorityCall=prior)

        if int(categ) != 0:
            calls = calls.filter(categoryCall=categ)

        context = {
            "calls": calls,
            "status": Status.objects.all(),
            "priorities": Priority.objects.all(),
            "categories": Category.objects.all()
 
        }



    return render(request, "calls/list.html", context)




def mycalls_list_search_view(request, *args, **kwargs):
    nerd = request.user.username

    mycalls = Call.objects.filter(nerdCall=nerd)

    if request.method == 'GET':
        status = request.GET.get('statusCall')
        prior = request.GET.get('priorityCall')
        categ = request.GET.get('categoryCall')


        if int(status) != 0:
            mycalls = mycalls.filter(statusCall=status)

        if int(prior) != 0:
            mycalls = mycalls.filter(priorityCall=prior)

        if int(categ) != 0:
            mycalls = mycalls.filter(categoryCall=categ)


    context = {
        "mycalls": mycalls,
        "status": Status.objects.all(),
        "priorities": Priority.objects.all(),
        "categories": Category.objects.all(),

        }


    return render(request, "mycalls/list.html", context)

# def closedcalls_view(request, *args, **kwargs):

#     return render(request, "closedcalls.html", {})

