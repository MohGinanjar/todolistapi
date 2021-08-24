from rest_framework.authentication import get_authorization_header , BaseAuthentication
from authentication.models import User
from rest_framework import exceptions
from django.conf import settings
import jwt

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed("Token Not Valid")

        token = auth_token[1]

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithm = 'HS256')

            username = payload['username']
            user = User.objects.get(username=username)

            return (user, token)

        except jwt.ExpiredSignatureError as ex : 
            raise exceptions.AuthenticatedFailed(
                'Token is Expired, Login Again'
            )
        except jwt.DecodeError as ex :
            raise exceptions.AuthenticatedFailed(
                'Token is invalid'
            )
        except User.DoesNotExist as no_user :
            raise exceptions.AuthenticatedFailed(
                'No such User'
            )

        return super().authenticate(request)
