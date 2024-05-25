from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from . import models
from django.urls import reverse_lazy
from .forms import MessageForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class AllMessages(LoginRequiredMixin, ListView):
    model = models.Message
    template_name = "messages/all_messages.html"
    context_object_name = "all_messages"
    ordering = "-sent_date"
    paginate_by = 30


class SingleMessage(LoginRequiredMixin, DetailView):
    template_name = "messages/single_message.html"
    context_object_name = "message"
    model = models.Message


class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = models.Message
    success_url = reverse_lazy('all-messages-page')


def save_message(request):
    if request.method == "POST":
        new_message_form = MessageForm(request.POST)
        if new_message_form.is_valid():
            new_message_form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)

    return redirect("home-page")
