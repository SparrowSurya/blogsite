from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from . import forms
from blog.models import Post


class UserRegistrationView(CreateView):
    """New user registration."""

    template_name = "user/register.html"
    success_url = reverse_lazy("user:login")
    form_class = forms.UserRegisterationForm


class UserLoginView(LoginView):
    """User login view."""

    form_class = forms.UserLoginForm
    template_name = "user/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """User logout view."""

    next_page = "blog:list"


class UserProfileView(DetailView):
    """User dashboard view."""

    model = User
    context_object_name = "user_obj"
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        if self.request.user == self.object:
            kwargs["posts"] = self.object.posts.all()
        else:
            kwargs["posts"] = self.object.posts.all().filter(status=Post.Status.PUBLISH)
        return kwargs