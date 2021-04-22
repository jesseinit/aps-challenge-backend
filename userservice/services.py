from typing import Dict

from rest_framework.exceptions import PermissionDenied
from utils.helpers import OneAPIAdapter, TokenManager
from userservice.models import User
from django.contrib.auth.hashers import make_password


class AuthenticationService:
    """ Service class to handle authentication actions """

    @classmethod
    def register_user(
        cls, username: str = None, email: str = None, password: str = None
    ) -> Dict:
        """ Service method to complete user signup """

        response = OneAPIAdapter.create_user(email=email, password=password)

        if response["success"] is False:
            raise PermissionDenied(
                dict(error="Couldnt not create your accout at this time")
            )

        created_user = User.objects.create(
            username=username.lower().replace(" ", ""),
            email=email.lower(),
            password=make_password(password),
        )

        return {
            "username": created_user.username,
            "email": created_user.email,
        }
