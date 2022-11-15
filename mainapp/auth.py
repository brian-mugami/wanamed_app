import os
from rest_framework import authentication, exceptions
import jwt

from .models import UsersModel

class UserAuth(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        token = request.COOKIES.get("jwt")
        
        if not token:
            return None
        
        try:
            payload = jwt.decode(token,os.environ.get("JWT_SECRET"),algorithms=["HS256"])
            
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        
        user = UsersModel.objects.get(id=payload["id"])
        
        return (user, None)