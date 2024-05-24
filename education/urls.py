from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.all_education_page, name="all-education-page"),
    path("create/", views.CreateEducation.as_view(), name="create-education-page"),
    path("update/<int:pk>/", views.UpdateEducation.as_view(), name="update-education-page"),
    path("delete/<pk>/", views.DeleteEducation.as_view(), name="delete-education-page")
]