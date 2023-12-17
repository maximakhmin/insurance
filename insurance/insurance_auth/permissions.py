from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user:
            if request.user.is_staff:
                return True
        return False


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user:
            return True
        return False
