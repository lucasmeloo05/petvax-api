from django.db import models

class Vaccine(models.Model):
    class Species(models.TextChoices):
        DOG = "dog", "Cachorro"
        CAT = "cat", "Gato"
        ALL = "all", "Todos"
        OTHER = "other", "Outro"

    name = models.CharField(max_length=120, unique=True)
    manufacturer = models.CharField(max_length=120, blank=True)
    species = models.CharField(max_length=20, choices=Species.choices, default=Species.ALL)
    recommended_interval_days = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
