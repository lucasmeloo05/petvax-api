from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Pet
from .serializers import PetSerializer
from .permissions import IsOwnerOrAdmin

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    search_fields = ["name", "breed"]
    ordering_fields = ["created_at", "name"]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Pet.objects.all()
        return Pet.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
