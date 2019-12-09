from django.urls import include , path
from mini_insta.views import HelloDjango , PostsView , PostDetailView

urlpatterns = [
    path('', HelloDjango.as_view(), name='test'),
    path('posts/',PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post_detail'),
]
