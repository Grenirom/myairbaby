from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user


class IsAdminOrAllowedPerson(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (request.user.is_authenticated and request.user.is_allowed)
    

