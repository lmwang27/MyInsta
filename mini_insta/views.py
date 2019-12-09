from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# render html
class HelloDjango(TemplateView):
    template_name = 'test.html'
    
