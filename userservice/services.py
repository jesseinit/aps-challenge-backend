from typing import Dict

from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from utils.helpers import OneAPIAdapter, TokenManager
from userservice.models import User
from django.contrib.auth.hashers import check_password, make_password


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
                dict(error="Couldnt not create your account at this time")
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

    @classmethod
    def login_user(cls, email: str = None, password: str = None) -> Dict:
        """ Service method to complete user signup """

        user = User.objects.filter(email=email.lower()).first()

        if user is None:
            raise AuthenticationFailed(dict(error="User credentials incorrect"))
        
        is_valid_password = check_password(password=password, encoded=user.password)
        if is_valid_password is False:
            raise PermissionDenied(dict(error="User credentials incorrect"))

        # If first time login grab and update access token from One API
        if user.api_token is None:
            response = OneAPIAdapter.login_user(email=email.lower(), password=password)
            if not response.get("access_token"):
                raise AuthenticationFailed(dict(error="User credentials incorrect"))
            user.update(api_token=response.get("access_token"))

        token = TokenManager.sign_token(payload={"uid": str(user.id)})

        return {"token": token}
