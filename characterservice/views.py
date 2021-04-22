# Create your views here.
import requests
from characterservice.services import CharacterService
from utils.helpers import ResponseManager

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action


class CharacterViewset(viewsets.ViewSet):
    @action(detail=False, methods=["get"], url_path="characters")
    def retrieve_characters(self, request):
        """ Retrieves all chracters """
        service_response = CharacterService.retrieve_characters(user=request.user)
        return ResponseManager.handle_response(
            message="Retrieval Success", data=service_response, status=200
        )
