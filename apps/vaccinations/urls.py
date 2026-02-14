from rest_framework.routers import DefaultRouter
from .views import VaccinationRecordViewSet

router = DefaultRouter()
router.register(r"", VaccinationRecordViewSet, basename="vaccinations")

urlpatterns = router.urls
