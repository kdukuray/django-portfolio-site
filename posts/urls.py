from django.urls import path
from . import views

urlpatterns = [
    path("all/<type>/", views.AllPosts.as_view(), name="all-posts-page"),
    path("create/", views.CreatePost.as_view(), name="create-post-page"),
    path("update/<int:pk>/", views.UpdatePost.as_view(), name="update-post-page"),
    path("singlepost/<pk>/", views.single_post, name="single-post-page"),
    path('delete/<pk>/', views.DeletePost.as_view(), name="delete-post-page"),
    path("newimage/", views.UploadImage.as_view(), name="upload-image-page"),
    path("allimages/", views.AllImages.as_view(), name="all-images-page")
]