from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import VaccinationRecord
from .serializers import VaccinationRecordSerializer
from .permissions import VaccinationAccessPermission
from .filters import VaccinationRecordFilter
from apps.accounts.roles import is_staff_user

class VaccinationRecordViewSet(viewsets.ModelViewSet):
    serializer_class = VaccinationRecordSerializer
    permission_classes = [IsAuthenticated, VaccinationAccessPermission]
    filterset_class = VaccinationRecordFilter

    def get_queryset(self):
        user = self.request.user
        qs = VaccinationRecord.objects.select_related("pet", "vaccine")
        if is_staff_user(user):
            return qs
        return qs.filter(pet__owner=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
