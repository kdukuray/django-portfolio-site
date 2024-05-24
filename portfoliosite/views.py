from django.shortcuts import render


def page_not_found(request, *args, **kwargs):
    return render(request, "home/page_not_found.html")