from rest_framework import permissions


#Override isOwner base permission to fit product.owner

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user