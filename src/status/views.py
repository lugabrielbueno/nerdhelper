from django.shortcuts import redirect, render
from .models import Status
from django import forms
from django.contrib import messages

# Create your views here.


def status_list_view(request, *args, **kwargs):

    status = {"status": Status.objects.all()}

    return render(request, 'status/list.html', status)


def status_create_view(request, *args, **kwargs):

    if request.method == 'POST':

        Stat = Status()
        Stat.statusName = request.POST['statusName']

        if not Stat.statusName:
            raise forms.ValidationError(
                messages.info(request, 'This field is required'))

        Stat.save()

        status = {"status": Status.objects.all()}

    return render(request, 'status/list.html', status)


def status_update_view(request, *args, **kwargs):

    if request.method == 'POST':

        Stat = Status.objects.get(id=request.POST['statusId'])
        Stat.statusName = request.POST['statusName']

        Stat.save()

        status = {"status": Status.objects.all()}

        messages.success(request, 'Successfully updated')

    return render(request, 'status/list.html', status)


def status_delete_view(request, id, *args, **kwargs):

    if request.method == 'POST':

        Stat = Status.objects.get(id=request.POST['statusId'])
        Stat.delete()

        messages.success(request, 'Successfully deleted')

        status = {"status": Status.objects.all()}

        return render(request, 'status/list.html', status)

    else:

        stat = {"stat": Status.objects.get(id=id)}

        return render(request, 'status/status_delete.html', stat)
