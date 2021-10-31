from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(10)
def home(request):
    """
    This function will return home template
    """
    return render(request, "enroll/home.html")
    
def contact(request):
    """
    This function will return contact template
    """
    return render(request, "enroll/contact.html")