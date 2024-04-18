from django.shortcuts import render

from .models import Position


def index(request):
    return render(request, 'users/index.html')


def md_employes(request):
    my_records = Position.objects.select_related(
        'employee',
        'subdivision',
    )
    return render(
        request,
        'users/md_employes.html',
        {
            'records': my_records,
        }
    )