from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
# Create your views here.
class CostomTemplateView(TemplateView):
    template_name = "school/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Moin Khan"
        context["roll"] = 101
        # we got out url id variable from kwargs
        print(kwargs)
        return context

class CustomRedirectView(RedirectView):
    pattern_name="homewithint"
    permanent = True
    query_string = True
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


        
    