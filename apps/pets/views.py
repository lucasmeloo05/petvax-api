from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Pet
from .serializers import (
    PetReadSerializer,
    PetWriteSerializer,
    PetWriteStaffSerializer,
)

def is_staff_user(user):
    return user.is_superuser or user.groups.filter(name="FUNCIONARIO").exists()


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()

    def get_queryset(self):
        user = self.request.user
        if is_staff_user(user):
            return Pet.objects.all()
        return Pet.objects.filter(owner=user)

    def get_serializer_class(self):
        user = self.request.user
        if self.action in ["list", "retrieve"]:
            return PetReadSerializer

        if is_staff_user(user):
            return PetWriteStaffSerializer
        return PetWriteSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if is_staff_user(user):
            owner_id = serializer.validated_data.pop("owner_id", None)
            if owner_id is not None:
                owner = User.objects.get(id=owner_id)
                serializer.save(owner=owner)
                return
            serializer.save(owner=user)
            return

        serializer.save(owner=user)

    def perform_update(self, serializer):
        user = self.request.user

        if is_staff_user(user):
            owner_id = serializer.validated_data.pop("owner_id", None)
            if owner_id is not None:
                owner = User.objects.get(id=owner_id)
                serializer.save(owner=owner)
                return
            serializer.save()
            return

        serializer.save(owner=user)
