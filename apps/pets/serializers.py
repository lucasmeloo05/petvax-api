from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)
    owner_username = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Pet
        fields = [
            "id",
            "owner_id",
            "owner_username",
            "name",
            "species",
            "breed",
            "birth_date",
            "sex",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "owner_id", "owner_username", "created_at", "updated_at"]
