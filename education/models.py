from django.db import models


class Education(models.Model):
    title = models.CharField(max_length=80)
    year = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return "Title: " + str(self.title)

