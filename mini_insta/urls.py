from django.urls import include , path
from mini_insta.views import (HelloDjango , PostsView , PostDetailView, PostCreateView, 
                              PostUpdateView,PostDeleteView, addLike,
                               UserDetailView, ExploreView,UserUpdateView, addComment, toggleFollow)

urlpatterns = [
    path('helloworld', HelloDjango.as_view(), name='test'),
    path('',PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post_upload'),
    path('post/update/<int:pk>',PostUpdateView.as_view(), name = 'post_update'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(), name = 'post_delete'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('user/<int:pk>', UserDetailView.as_view(), name ='profile'),
    path('user/update/<int:pk>', UserUpdateView.as_view(), name ='edit_profile'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('togglefollow', toggleFollow, name='togglefollow'),

]
