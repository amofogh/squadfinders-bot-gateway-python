from rest_framework.permissions import BasePermission

class HasAPIKey(BasePermission):
    """
    Custom permission to check for API key authentication.
    """
    
    def has_permission(self, request, view):
        # Allow access if the request is authenticated with API key
        return request.auth is not None