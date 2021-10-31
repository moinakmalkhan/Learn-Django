"""GenericClassBasedView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    # path("",views.TemplateView.as_view(template_name="school/home.html")),
    path("<int:id>",views.CostomTemplateView.as_view(extra_context={'course':'Computer Science'}),name='homewithint'),
    path("",views.CostomTemplateView.as_view(extra_context={'course':'Computer Science'}),name='home'),
    # path("home/",views.RedirectView.as_view(url="/")),
    # path("index/",views.RedirectView.as_view(url="/")),
    # path("home/",views.RedirectView.as_view(pattern_name='home')),
    # path("index/",views.RedirectView.as_view(pattern_name='home')),
    # path("",views.CostomTemplateView.as_view(extra_context={'course':'Computer Science'})),

    path("home/<int:id>", views.CustomRedirectView.as_view()),
    path('admin/', admin.site.urls),
]
