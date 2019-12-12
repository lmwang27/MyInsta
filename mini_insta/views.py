from annoying.decorators import ajax_request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from mini_insta.models import Post, InstaUser, Like, UserConnection,Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mini_insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# render html
class HelloDjango(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = "index.html"
    login_url = "login"

    """
    def get_queryset(self):
        current_user = self.request.user
        following = set()
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)
    """

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "post_create.html"
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("posts")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }


@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }

class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_profile.html'


class ExploreView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'explore.html'
    login_url = 'login'

    def get_queryset(self):
        return Post.objects.all().order_by('-posted_on')[:20]

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = InstaUser
    template_name = 'edit_profile.html'
    fields = ['profile_pic', 'username']
    login_url = 'login'







