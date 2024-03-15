from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    list_display = ["id", "title", "description", "status", "creator", "created_at", "updated_at"]
