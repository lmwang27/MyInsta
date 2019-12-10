from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from mini_insta.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
# render html
class HelloDjango(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = "index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = '__all__'



