from django.contrib import admin
from .models import Vaccine

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "species", "recommended_interval_days", "created_at")
    search_fields = ("name", "manufacturer")
    list_filter = ("species",)
