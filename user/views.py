from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from typing import Dict, Any

from . import forms
import blog.models


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


class UserDashboardView(LoginRequiredMixin, TemplateView):
    """User dashboard view."""

    template_name = "user/dashboard.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = blog.models.Post.objects.all().filter(author=self.request.user)
        return context
