from typing import Dict
from utils.exceptions import UnavailableResourceException
import jwt
from django.conf import settings
from userservice.models import User
from rest_framework import serializers
from rest_framework.response import Response
import requests


class TokenManager:
    @classmethod
    def sign_token(cls, payload: dict = {}, exipire_at=None) -> str:
        token = jwt.encode(
            {
                **payload,
                "iat": settings.JWT_SETTINGS["ISS_AT"](),
                "exp": exipire_at or settings.JWT_SETTINGS["EXP_AT"](),
            },
            settings.SECRET_KEY,
        )
        return token

    @classmethod
    def decode_token(cls, token):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])


class FieldValidators:
    """ Custom Validators for Serializer Fields """

    @staticmethod
    def validate_existing_email(email):
        user_email = email.strip()
        user = User.objects.filter(email=user_email).exists()
        if user:
            raise serializers.ValidationError(
                "A user has already registered with this email address"
            )
        return user_email

    @staticmethod
    def validate_existing_username(username):
        user_username = username.strip()
        user = User.objects.filter(username=user_username).exists()
        if user:
            raise serializers.ValidationError(
                "A user has already registered with this username"
            )
        return user_username

    @staticmethod
    def validate_non_existing_email(email):
        user = User.objects.filter(email=email).exists()
        if not user:
            raise serializers.ValidationError("This user does not exist")
        return email


class ResponseManager:
    """ Helper class to prepare endpoint response """

    @staticmethod
    def handle_response(message=None, data=None, error=None, status=200) -> Response:
        if error:
            return Response({"message": message, "error": error}, status=status)
        return Response({"message": message, "data": data}, status=status)


class OneAPIAdapter:
    """ Adapter Class that interface with One API Dev Resources """

    ONE_API_BASE = settings.ONE_API_BASE

    @classmethod
    def create_user(cls, email: str = None, password: str = None) -> Dict:
        try:
            response = requests.post(
                url=cls.ONE_API_BASE + f"/auth/register",
                json={
                    "email": email,
                    "password": password,
                    "passwordValidate": password,
                },
                timeout=5,
            )
            if not response.ok:
                raise UnavailableResourceException(
                    dict(error=response.json()["message"])
                )
            return response.json()
        except Exception:
            raise UnavailableResourceException(dict(error=response.json()["message"]))

    @classmethod
    def login_user(cls, email: str = None, password: str = None) -> Dict:
        try:
            response = requests.post(
                url=cls.ONE_API_BASE + f"/auth/login",
                json={
                    "email": email,
                    "password": password,
                },
                timeout=5,
            )
            if not response.ok:
                raise UnavailableResourceException(
                    dict(error=response.json()["message"])
                )
            return response.json()
        except Exception:
            raise UnavailableResourceException(dict(error=response.json()["message"]))
