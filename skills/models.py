from django.db import models

skill_choices = [
    ("Lang", "Language"),
    ("Tech", "Technology")
]


class Skill(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=skill_choices, default="Lang")
    image = models.ImageField(upload_to="skills_images")

    def __str__(self):
        return f"{self.name} -> ({self.type})"

