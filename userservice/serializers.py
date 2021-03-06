from userservice.models import User
from rest_framework import serializers
from utils.helpers import FieldValidators


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=2, max_length=50, validators=[FieldValidators.validate_existing_username]
    )
    email = serializers.EmailField(validators=[FieldValidators.validate_existing_email])
    password = serializers.CharField(min_length=8, max_length=16)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[FieldValidators.validate_non_existing_email])
    password = serializers.CharField(min_length=8, max_length=16)
