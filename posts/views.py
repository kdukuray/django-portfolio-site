from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AllPosts(ListView):
    template_name = "posts/all_posts.html"
    context_object_name = "all_posts"
    model = models.Post
    ordering = "-last_updated"
    paginate_by = 10

    def get_queryset(self):
        query_by = self.kwargs.get("type")
        query_set = models.Post.objects.order_by("-last_updated").filter(type=query_by)
        return query_set


class CreatePost(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ["title", "content", "type"]
    template_name = "posts/create_post.html"
    success_url = reverse_lazy('all-posts-page', kwargs={"type": "blog"})


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = models.Post
    fields = ["title", "content", "type"]
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("all-posts-page", kwargs={"type": "blog"})


def single_post(request, pk):
    post = models.Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, "posts/single_post.html", context=context)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('all-posts-page', kwargs={"type": "blog"})


class UploadImage(LoginRequiredMixin, CreateView):
    model = models.ImageObj
    fields = "__all__"
    success_url = reverse_lazy("all-images-page")
    template_name = "posts/upload_image.html"


class AllImages(LoginRequiredMixin, ListView):
    model = models.ImageObj
    template_name = "posts/all_images.html"
    context_object_name = "all_images"
    paginate_by = 10
