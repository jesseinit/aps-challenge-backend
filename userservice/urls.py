from userservice.views import AuthenticationViewset
from django.conf.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)

router.register(r"user", AuthenticationViewset, basename="authentication")

urlpatterns = [
    re_path(r"", include(router.urls)),
]
