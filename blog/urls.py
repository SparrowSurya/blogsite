from django.urls import path

from . import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete"),

    # url(r"^$", views.PostListView.as_view(), name="post_list"),
    # url(r"^about", views.AboutView.as_view(), name="about"),
    # url(r"^post/(?P<pk>\d+)/$",views.PostDetailView.as_view(),name="post_detail"),
    # url(r"^post/(?P<pk>\d+)/edit",views.PostUpdateView.as_view(),name="post_update"),
    # url(r"^post/(?P<pk>\d+)/delete",views.PostDeleteView.as_view(),name="post_delete"),
    # url(r"^post/create/$",views.PostCreateView.as_view(),name="post_create"),
    # url(r"^draft",views.DraftView.as_view(),name="draft"),
    # url(r"^post/(?P<pk>\d+)/comment",views.add_comment,name="comment"),
    # url(r"^comment/(?P<pk>\d+)/approve/$",views.comment_approve,name="comment_approve"),
    # url(r"^comment/(?P<pk>\d+)/remove/$",views.comment_remove,name="comment_remove"),
    # url(r"^post/(?P<pk>\d+)/publish/$",views.publish,name="post_publish")
]
