import jwt
from rest_framework import authentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from common.models import ExtendedUser


class JWTAuthentication(authentication.BaseAuthentication):
    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                jwt=token,
                key=settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM],
            )
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError) as e:
            raise AuthenticationFailed(e)

        return decoded_token

    def authenticate(self, request):
        token = request.headers['Authorization'].split()[1]
        decoded_token = self.decode_token(token=token)

        try:
            user = ExtendedUser.objects.get(pk=decoded_token['sub'])
        except ExtendedUser.DoesNotExist:
            raise AuthenticationFailed('No such user')

        return user, None
