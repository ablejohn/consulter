from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('receive-message', views.receive_message, name="receive_message"),
    path('portfolio', views.portfolio, name="portfolio")
]