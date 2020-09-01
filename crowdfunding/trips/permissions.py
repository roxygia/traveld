from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organiser == request.user

class IsTripMateOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.trip_mate == request.user
   

    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     if obj.organiser == request.user:
    #         return True
    #     return False
    #or request.user.is_superuse