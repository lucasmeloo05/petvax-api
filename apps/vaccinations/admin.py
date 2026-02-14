from django.contrib import admin
from .models import VaccinationRecord

@admin.register(VaccinationRecord)
class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "pet", "vaccine", "applied_at", "dose_number", "created_by")
    search_fields = ("pet__name", "vaccine__name", "created_by__username")
    list_filter = ("applied_at", "vaccine")
