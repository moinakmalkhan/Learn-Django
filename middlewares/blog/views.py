from django.shortcuts import render, HttpResponse

# Create your views here.
def home(req):
    print("Hello from view")
    a = 10/0
    return HttpResponse("Hello world")