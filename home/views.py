from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from skills import models as skillmodel
from education import models as educationmodel
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# By default, Python might not be able to find the packages in the skills and education package
# because python doesn't consider the current working directory to be a package
# To fix this, you may have the directory containing your package to the Python path
# This is done using the following code:
# import sys
# sys.path.append("..")
# - Here's a link to a stack overflow article that addresses it:
# https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import


def home_page(request):
    about = models.AboutMe.objects.get(pk=1)
    all_languages = skillmodel.Skill.objects.filter(type="Lang")
    all_technologies = skillmodel.Skill.objects.filter(type="Tech")
    all_education = educationmodel.Education.objects.all()
    context = {
        "about": about,
        "all_languages": all_languages,
        "all_technologies": all_technologies,
        "all_education": all_education,
    }
    return render(request, "home/home.html", context=context)


class UpdateAboutPage(LoginRequiredMixin, UpdateView):
    model = models.AboutMe
    fields = ["content", "image"]
    template_name = "home/update_about.html"
    success_url = reverse_lazy("home-page")


class LogoutConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = "home/logout_confirmation.html"

