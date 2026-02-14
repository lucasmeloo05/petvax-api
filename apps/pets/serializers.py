from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet

class PetReadSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(source="owner.id", read_only=True)
    owner_username = serializers.CharField(source="owner.username", read_only=True)
    owner_email = serializers.EmailField(source="owner.email", read_only=True)

    class Meta:
        model = Pet
        fields = [
            "id",
            "owner_id",
            "owner_username",
            "owner_email",
            "name",
            "species",
            "breed",
            "birth_date",
            "sex",
            "created_at",
            "updated_at",
        ]


class PetWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "birth_date", "sex"]


class PetWriteStaffSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(required=False)

    class Meta:
        model = Pet
        fields = ["owner_id", "name", "species", "breed", "birth_date", "sex"]

    def validate_owner_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("Usuário (owner_id) não encontrado.")
        return value
