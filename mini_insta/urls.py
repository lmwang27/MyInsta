from django.urls import include , path
from mini_insta.views import HelloDjango , PostsView , PostDetailView, PostCreateView, PostUpdateView,PostDeleteView, addLike

urlpatterns = [
    path('helloworld', HelloDjango.as_view(), name='test'),
    path('',PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post_upload'),
    path('post/update/<int:pk>',PostUpdateView.as_view(), name = 'post_update'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(), name = 'post_delete'),
    path('like', addLike, name='addLike'),

]
