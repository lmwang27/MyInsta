from django.urls import include , path
from mini_insta.views import HelloDjango

urlpatterns = [
    path('', HelloDjango.as_view(), name='test')
]
