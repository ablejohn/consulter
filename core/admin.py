from django.contrib import admin
from . import models


@admin.register(models.OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(models.ContactMessages)
class ContactMessages(admin.ModelAdmin):
    list_display = ["name", "subject", "created_at", "updated_at"]