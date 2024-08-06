from django import forms

from . import models


class PostCreateForm(forms.ModelForm):
    """Form for post creation."""

    class Meta:
        model = models.Post
        fields = ("title", "text")


class PostUpdateForm(forms.ModelForm):
    """Form for post updation."""

    class Meta:
        model = models.Post
        fields = ("title", "text", "status")


class PostCommentForm(forms.ModelForm):
    """Form for post comments"""

    class Meta:
        model = models.Comment
        fields = ("text",)
