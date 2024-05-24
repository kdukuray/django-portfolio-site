from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("updateabout/<int:pk>/", views.UpdateAboutPage.as_view(), name="update-about-page"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login-page"),
    path("logout/confirmation/", views.LogoutConfirmationView.as_view(), name="logout-confirmation-page"),
    path("logout/", LogoutView.as_view(template_name="home/logout_success.html"), name="logout-page"),
]