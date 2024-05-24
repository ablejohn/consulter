from django.contrib import admin
from . import models


class PostTagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


admin.site.register(models.PostTag, PostTagAdmin)
admin.site.register(models.Post, PostAdmin)
