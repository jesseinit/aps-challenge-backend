from rest_framework.exceptions import APIException
from rest_framework.status import (
    HTTP_503_SERVICE_UNAVAILABLE,
)


class UnavailableResourceException(APIException):
    status_code = HTTP_503_SERVICE_UNAVAILABLE
    default_detail = {"error": "This resource is down. Retry again"}
