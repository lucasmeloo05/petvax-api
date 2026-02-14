from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Vaccine
from .serializers import VaccineSerializer
from .permissions import IsStaffOrReadOnly

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
    search_fields = ["name", "manufacturer"]
    ordering_fields = ["name", "created_at"]
