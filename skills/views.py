from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def all_skills_page(request):
    all_languages = models.Skill.objects.filter(type="Lang")
    all_technologies = models.Skill.objects.filter(type="Tech")
    context = {"all_languages": all_languages,
               "all_technologies": all_technologies}
    return render(request, "skills/all_skills.html", context=context)


class CreateSkill(LoginRequiredMixin, CreateView):
    model = models.Skill
    template_name = "skills/create_skill.html"
    success_url = reverse_lazy("all-skills-page")
    fields = ["image", "name", "type"]


class UpdateSkill(LoginRequiredMixin, UpdateView):
    model = models.Skill
    template_name = "skills/create_skill.html"
    success_url = reverse_lazy("all-skills-page")
    fields = ["image", "name", "type"]


class DeleteSkill(LoginRequiredMixin, DeleteView):
    model = models.Skill
    success_url = reverse_lazy("all-skills-page")
