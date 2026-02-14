from rest_framework import serializers
from .models import Vaccine

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = [
            "id",
            "name",
            "manufacturer",
            "species",
            "recommended_interval_days",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
