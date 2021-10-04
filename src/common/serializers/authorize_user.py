from datetime import datetime

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from common.models import ExtendedUser


class AuthorizeUser(serializers.ModelSerializer):
    access_token = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=256, write_only=True)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'password', 'access_token')

    @staticmethod
    def generate_token(user: ExtendedUser) -> str:
        payload = {
            'sub': user.pk,
            'is_doctor': user.is_doctor,
            'exp': round((datetime.now() + settings.EXPIRATION_TIME).timestamp()),
        }
        encoded_token = jwt.encode(
            payload=payload,
            key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )
        return encoded_token

    def create(self, validated_data) -> ExtendedUser:
        user = authenticate(request=self.context['request'], **validated_data)
        if not user:
            raise AuthenticationFailed()
        user.access_token = self.generate_token(user=user)
        return user

