from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.


def Biblio(request):
    ip_address = '192.168.1.73'
    port = '8000'
    livres = list(Livre.objects.all().values())

    for livre in livres:
        livre['document'] = f'http://{ip_address}:{port}/api/v1/books/'
        livre['image'] = f'http://{ip_address}:{port}/api/v1/books/'
    context = {   
    "livres" : livres,
    }
    
    return JsonResponse(context['livres'], safe=False)