from django.contrib import admin
from django.urls import path ,include
from mini_insta.views import HelloDjango

urlpatterns = [
    path('', HelloDjango.as_view(), name='test')
]
