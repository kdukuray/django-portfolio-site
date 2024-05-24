from django.db import models


class Message(models.Model):
    sender_name = models.CharField(max_length=30)
    sender_email = models.EmailField(max_length=30)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now=True)

# Create your models here.
