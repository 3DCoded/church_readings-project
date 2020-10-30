from django.shortcuts import render
from .readings import getReadings
import os
from django.http import HttpResponse

__path__ = os.path.dirname(os.path.abspath(__file__))

def js1(request):
    with open(os.path.join(__path__, 'static', 'jquery-3.5.1.slim.min.js')) as file: return HttpResponse(file.read(), content_type = 'text/javascript')

def js2(request):
    with open(os.path.join(__path__, 'static', 'popper.min.js')) as file: return HttpResponse(file.read(), content_type = 'text/javascript')

def js3(request):
    with open(os.path.join(__path__, 'static', 'bootstrap.min.js')) as file: return HttpResponse(file.read(), content_type = 'text/javascript')

handler404 = lambda request, exception: render(request, '404.html', {'error': exception.args[0]['path']}, status = 404)
handler500 = lambda request: render(request, '404.html', status = 404)

def home(request):
    r = getReadings()
    return render(request, 'home.html', {
        'ves': r['Vespers Gospel'],
        'mat': r['Matins Gospel'],
        'paul': r['Pauline Epistle'],
        'cath': r['Catholic Epistle'],
        'acts': r['Acts'],
        'synx': r['Synxarium'],
        'gos': r['Gospel'],
    })