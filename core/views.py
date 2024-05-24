from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'core/index.html')


def services(request: HttpRequest):
    all_services = models.OurServices.objects.all()
    return render(request, 'core/services.html', {"all_services": all_services})


def about(request: HttpRequest):
    return render(request, 'core/about.html')


def contact(request: HttpRequest):
    return render(request, 'core/contact.html')


def receive_message(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        new_message = models.ContactMessages.objects.create(name=name, email=email, subject=subject, message=message)
        new_message.save()
        messages.success(request, "Your message has been received.")
        return redirect("core:contact")


def portfolio(request: HttpRequest):
    return render(request, "core/portfolio.html")
