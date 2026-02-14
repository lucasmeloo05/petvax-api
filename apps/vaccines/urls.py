from rest_framework.routers import DefaultRouter
from .views import VaccineViewSet

router = DefaultRouter()
router.register(r"", VaccineViewSet, basename="vaccines")

urlpatterns = router.urls
