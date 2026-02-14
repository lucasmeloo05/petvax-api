from rest_framework import serializers

from apps.vaccines.models import Vaccine
from .models import VaccinationRecord


class VaccinationRecordSerializer(serializers.ModelSerializer):
    created_by_id = serializers.IntegerField(read_only=True)

    pet_name = serializers.CharField(source="pet.name", read_only=True)
    vaccine_name = serializers.CharField(source="vaccine.name", read_only=True)

    class Meta:
        model = VaccinationRecord
        fields = [
            "id",
            "pet",
            "pet_name",
            "vaccine",
            "vaccine_name",
            "applied_at",
            "dose_number",
            "next_due_at",
            "notes",
            "created_by_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "pet_name",
            "vaccine_name",
            "created_by_id",
            "created_at",
            "updated_at",
        ]

    def validate_pet(self, pet):
        # Quem decide se pode criar/editar é a permission (VaccinationAccessPermission)
        return pet

    def validate_vaccine(self, vaccine: Vaccine):
        # Validações extras, se quiser
        return vaccine
