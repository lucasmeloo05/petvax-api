from django.conf import settings
from django.db import models

from apps.pets.models import Pet
from apps.vaccines.models import Vaccine

class VaccinationRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT, related_name="applications")

    applied_at = models.DateField()
    dose_number = models.PositiveIntegerField(default=1)
    next_due_at = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_vaccinations",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-applied_at", "-created_at"]
        indexes = [
            models.Index(fields=["pet", "applied_at"]),
            models.Index(fields=["vaccine", "applied_at"]),
        ]

    def __str__(self):
        return f"{self.pet.name} - {self.vaccine.name} ({self.applied_at})"
