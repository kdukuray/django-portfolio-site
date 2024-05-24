from django.forms import ModelForm
from . import models


class MessageForm(ModelForm):
    class Meta:
        model = models.Message
        fields = ["sender_name", "sender_email", "content"]