from django.db import models


post_choices = [
    ("blog", "Blog"),
    ("project", "Project")
]


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10, choices=post_choices, default="blog")

    def __str__(self):
        return f"{self.title} - {self.type}"


class ImageObj(models.Model):
    purpose = models.CharField(max_length=30)
    source = models.ImageField(upload_to="all_images")
    date_uploaded = models.DateTimeField(auto_now_add=True)
