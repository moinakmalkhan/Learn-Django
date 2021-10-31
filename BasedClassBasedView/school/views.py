from django.shortcuts import render,HttpResponse
from django.views import View


class Home(View):
    name=''
    def get(self, requset):
        return HttpResponse(f"Hello from class based view - {self.name}")


