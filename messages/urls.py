from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.AllMessages.as_view(), name="all-messages-page"),
    path("save/", views.save_message, name="save-message-route"),
    path("<pk>/", views.SingleMessage.as_view(), name="single-message-page"),
    path("delete/<pk>/", views.DeleteMessage.as_view(), name="delete-message-page"),

]