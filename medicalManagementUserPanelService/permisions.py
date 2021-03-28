from rest_framework.permissions import BasePermission


class DoctorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.user_type == 2:
            return True
        return False


class NormalUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.user_type == 1:
            return True
        return False
