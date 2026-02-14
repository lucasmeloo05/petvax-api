from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.accounts.roles import is_staff_user

class VaccinationAccessPermission(BasePermission):
    """
    -FUNCIONARIO/superuser: pode tudo
    -CLIENTE: apenas leitura (GET)
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return is_staff_user(request.user)

    def has_object_permission(self, request, view, obj):
        if is_staff_user(request.user):
            return True
        #Cliente só pode ver vacinação do próprio pet
        return request.method in SAFE_METHODS and obj.pet.owner_id == request.user.id
