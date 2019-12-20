from rest_framework import permissions

class AnonymousPermission(permissions.BasePermission):
    """
    Non Anonymous Users.
    """
    message = "You are already registered. Please logout and try again."

    def has_permission(self, request, view):
        print(not request.user.is_authenticated)
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object level permissions that only allow owner of object to edit it.
    """

    message = "You cannot edit this object, since you are not the owner of this object."

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.owner == request.user
