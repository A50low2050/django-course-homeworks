from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class AdminPhone(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'release_date', 'lte_exists', 'slug']
    prepopulated_fields = {'slug': ('name',)}
