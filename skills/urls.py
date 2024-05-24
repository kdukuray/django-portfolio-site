from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.all_skills_page, name="all-skills-page"),
    path("create/", views.CreateSkill.as_view(), name="create-skill-page"),
    path("update/<int:pk>/", views.UpdateSkill.as_view(), name="update-skill-page"),
    path("delete/<int:pk>/", views.DeleteSkill.as_view(), name="delete-skill-page"),
]

