from userservice.services import AuthenticationService
from utils.helpers import ResponseManager
from userservice.serializers import RegisterUserSerializer

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action


class AuthenticationViewset(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()

    @action(detail=False, methods=["post"], url_path="register")
    def register_user(self, request):
        """ View that handles account creation """
        serialized_data = RegisterUserSerializer(data=request.data)
        if not serialized_data.is_valid():
            return ResponseManager.handle_response(
                error=serialized_data.errors, status=400
            )
        service_response = AuthenticationService.register_user(
            **serialized_data.data,
        )
        return ResponseManager.handle_response(
            message="Registration Successful", data=service_response, status=201
        )
