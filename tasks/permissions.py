from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        # write permissions are only granted to owners of the subject
        return obj.owner==request.user