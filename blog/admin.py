from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """Admin interface for the blog post."""

    list_display = ("title", "author", "creation_date", "status")
    ordering = ("published_date", "creation_date")
    readonly_fields = ("creation_date", "updation_date", "published_date")
    list_filter = ("status",)

    fieldsets = (
        (None, {
            "fields": ("title", "author", "status"),
        }),
        ("Timestamp", {
            "fields": ("creation_date", "updation_date", "published_date"),
        }),
        ("Content", {
            "fields": ("text",)
        })
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface fr the blog post comment."""

    list_display = ("post_title", "user", "text")
    ordering = ("creation_date",)
    readonly_fields = ("creation_date",)

    fieldsets = (
        (None, {
            "fields": ("post_title", "user")
        }),
        ("Timestamp", {
            "fields": ("creation_date",)
        }),
        ("Content", {
            "fields": ("text",)
        })
    )

    def post_title(self, obj):
        return obj.post.title