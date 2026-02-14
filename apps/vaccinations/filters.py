import django_filters
from .models import VaccinationRecord

class VaccinationRecordFilter(django_filters.FilterSet):
    applied_at_after = django_filters.DateFilter(field_name="applied_at", lookup_expr="gte")
    applied_at_before = django_filters.DateFilter(field_name="applied_at", lookup_expr="lte")

    class Meta:
        model = VaccinationRecord
        fields = ["pet", "vaccine", "applied_at_after", "applied_at_before"]
