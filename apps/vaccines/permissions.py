from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.accounts.roles import is_staff_user

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return is_staff_user(request.user)
