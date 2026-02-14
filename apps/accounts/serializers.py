from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.accounts.roles import ROLE_CLIENTE

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )

        #Colocar usuário como Cliente
        cliente_group = Group.objects.get(name=ROLE_CLIENTE)
        user.groups.add(cliente_group)

        return user
