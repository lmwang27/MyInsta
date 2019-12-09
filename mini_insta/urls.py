from django.urls import include , path
from mini_insta.views import HelloDjango , PostsView

urlpatterns = [
    path('', HelloDjango.as_view(), name='test'),
    path('posts/',PostsView.as_view(), name = 'posts')
]
