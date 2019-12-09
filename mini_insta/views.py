from django.shortcuts import render
from django.views.generic import TemplateView , ListView, DetailView
from mini_insta.models import Post

# Create your views here.
# render html
class HelloDjango(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = "index.html"

