from django.shortcuts import render
from .forms import WebUserForm

# Create your views here.


def registration(request):
    fm = WebUserForm()
    if request.method == 'POST':
        fm = WebUserForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(name)
            print(email)
            print(password)
        fm = WebUserForm()
    context = {
        "form": fm
    }
    return render(request, "enroll/index.html", context)
