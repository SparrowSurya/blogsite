from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms

# from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse,HttpResponseRedirect
# from django.urls import reverse,reverse_lazy
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login,logout,authenticate
# from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView, CreateView

# from . import forms


class PostListView(ListView):
    """Posts list view containing posts that are published."""

    model = models.Post
    context_object_name = "posts"
    template_name = "blog/list.html"
    queryset = models.Post.objects.all().filter(status=models.Post.Status.PUBLISH)


class PostCreateView(LoginRequiredMixin, CreateView):
    """Post create view."""

    model = models.Post
    form_class = forms.PostCreateForm
    template_name = "blog/create.html"

    def get_success_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDetailView(DetailView, FormView):
    """Post details view."""

    model = models.Post
    context_object_name = "post"
    form_class = forms.PostCommentForm
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["comments"] = self.object.comments.all()
        kwargs['form'] = self.get_form()
        return kwargs

    def get_success_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user
        comment.save()
        return redirect(self.get_success_url())


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Draft view of the post."""

    model = models.Post
    form_class = forms.PostUpdateForm
    context_object_name = "post"
    template_name = "blog/update.html"

    def get_success_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Delete view of the post."""

    model = models.Post
    template_name = "blog/delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("user:dashboard")


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     """Create user comments."""

#     model = models.Comment
#     template_name = "blog/delete.html"

#     def get_success_url(self) -> str:
#         return reverse("blog:detail", kwargs={"pk": self.object.post.pk})


# def user_login(request):
#     context = {}

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         if user := authenticate(username=username, password=password):
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect("/")
#             else:
#                 return HttpResponse("blog/post_list.html")
#         else:
#             return render(request,"registeration/login.html",{})

#     else:
#         return render(request,"registeration/login.html",{})

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("blog:post_list"))

# @login_required
# def publish(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     post.publish()
#     post.save()
#     return HttpResponseRedirect("/draft")

# class AboutView(TemplateView):
#     template_name = "blog/post_about.html"


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"

# class PostCreateView(LoginRequiredMixin,CreateView):
#     login_url = "/login/"
#     redirect_field_name = "blog:post_detail"
#     form_class = PostForm
#     model = Post
#     template_name = "blog/post_create.html"

# class PostUpdateView(LoginRequiredMixin,UpdateView):
#     model = Post
#     template_name = "blog/post_update.html"

#     login_url = "/login/"
#     redirect_field_name = "blog/post_detail.html"
#     form_class = PostForm

# class PostDeleteView(LoginRequiredMixin,DeleteView):
#     model = Post
#     success_url = reverse_lazy("blog:post_list")


# class DraftView(LoginRequiredMixin,ListView):
#     model = Post
#     context_object_name = "DraftL"
#     template_name = "blog/post_draft_list.html"

#     login_url = "/login/"
#     redirect_field_name = "blog/post_list.html"

#     def get_queryset(self):
#         return Post.objects.filter(published_date__isnull=True).order_by("published_date")

# #######################################################################
# ######################  COMMENTS  #####################################


# def add_comment(request,pk):
#     post = get_object_or_404(Post,pk=pk)

#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author=request.user.username
#             comment.save()

#             return redirect("blog:post_detail",pk=post.pk)

#     else:
#         form = CommentForm()
#         return render(request,"blog/post_detail.html",{"form1":form,"post":post})

# @login_required
# def comment_approve(request,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     comment.approve()
#     pks=comment.post.pk
#     return redirect("blog:post_detail",pk=pks)

# @login_required
# def comment_remove(request,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect("blog:post_detail",pk=post_pk)
