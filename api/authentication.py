from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import os

class APIKeyAuthentication(BaseAuthentication):
    """
    Simple API Key authentication.
    Clients should authenticate by passing the API key in the "X-API-Key" header.
    """
    
    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        
        if not api_key:
            return None
            
        expected_api_key = os.getenv('API_KEY', 'your-secret-api-key-here')
        
        if api_key != expected_api_key:
            raise AuthenticationFailed('Invalid API key')
            
        # Return a tuple of (user, token) - we'll use None for user since we don't need it
        return (None, api_key)

    def authenticate_header(self, request):
        return 'X-API-Key'