from rest_framework.permissions import BasePermission


class IsVerifiedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_verified


class IsAdminUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"