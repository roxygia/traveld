from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(Self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return {
            obj.organiser == request.user
            or request.user.is_superuser
        }

