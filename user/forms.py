from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterationForm(UserCreationForm):
    """Form for user registeration."""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


class UserLoginForm(AuthenticationForm):
    """User login form."""