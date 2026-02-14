from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def api_root(request):
    return JsonResponse({
        "message": "PetVax API",
        "endpoints": {
            "auth": "/api/auth/token/",
            "accounts": "/api/accounts/",
            "pets": "/api/pets/",
            "vaccines": "/api/vaccines/",
            "vaccinations": "/api/vaccinations/"
        }
    })

urlpatterns = [
    #Root
    path("", api_root, name="api-root"),

    #Admin
    path("admin/", admin.site.urls),

    #Auth (JWT)
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    #Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    #API apps
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/pets/", include("apps.pets.urls")),
    path("api/vaccines/", include("apps.vaccines.urls")),
    path("api/vaccinations/", include("apps.vaccinations.urls")),
]

