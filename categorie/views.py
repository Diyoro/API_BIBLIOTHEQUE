from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.


def Biblio(request):
    context = {   
    "livres" : list(Livre.objects.all().values()),
    }
    
    return JsonResponse(context['livres'], safe=False)