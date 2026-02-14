from django.conf import settings
from django.db import models

class Pet(models.Model):
    class Species(models.TextChoices):
        DOG = "dog", "Cachorro"
        CAT = "cat", "Gato"
        OTHER = "other", "Outro"

    class Sex(models.TextChoices):
        MALE = "male", "Macho"
        FEMALE = "female", "Fêmea"
        UNKNOWN = "unknown", "Não informado"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pets",
    )
    name = models.CharField(max_length=120)
    species = models.CharField(max_length=20, choices=Species.choices)
    breed = models.CharField(max_length=120, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=Sex.choices, default=Sex.UNKNOWN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["owner", "name"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.owner})"
