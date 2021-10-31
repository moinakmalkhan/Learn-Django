from django.shortcuts import render, HttpResponse
from . import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user=['Moin',"Khan"])
    return HttpResponse("Hello world")