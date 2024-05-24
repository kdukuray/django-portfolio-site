from django.shortcuts import render
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def all_education_page(request):
    all_education = models.Education.objects.all()
    context = {"all_education": all_education}
    return render(request, "education/all_education.html", context=context)


class CreateEducation(LoginRequiredMixin, CreateView):
    model = models.Education
    fields = "__all__"
    template_name = "education/create_education.html"
    success_url = reverse_lazy("all-education-page")


class UpdateEducation(LoginRequiredMixin, UpdateView):
    model = models.Education
    fields = "__all__"
    template_name = "education/create_education.html"
    success_url = reverse_lazy("all-education-page")


class DeleteEducation(LoginRequiredMixin, DeleteView):
    model = models.Education
    success_url = reverse_lazy("all-education-page")
