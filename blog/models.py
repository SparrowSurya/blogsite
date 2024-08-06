from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Post(models.Model):
    """Blog post model."""

    class Status(models.TextChoices):
        """Status of blog post."""

        DRAFT = "DRAFT", _("Draft")
        PUBLISH = "PUBLISH", _("Publish")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=7, choices=Status, default=Status.DRAFT)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "posts"

    @property
    def is_published(self) -> bool:
        """Check is blog is published."""
        return self.published_date is not None

    def save(self, *args, **kwargs):
        """
        Save the instance.

        It also checks if the blog post has been published or not.
        """
        if not self.is_published and self.status == self.Status.PUBLISH:
            self.published_date = timezone.now()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment of blog post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    text = models.TextField(max_length=510)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.text
