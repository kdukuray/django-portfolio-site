from django.db import models


# This is the model that stores the "about me" section on the home page.
# It should only have record saved in it at all times
# it is to be saved as plain text in markdown which will be transpiled into html later
class AboutMe(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="auxilliary_images")

    def __str__(self):
        return "About Page Descrption"

