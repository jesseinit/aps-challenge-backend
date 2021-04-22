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
        """ Retrieves all characters """
        service_response = CharacterService.retrieve_characters(user=request.user)
        return ResponseManager.handle_response(
            message="Retrieval Success", data=service_response, status=200
        )

    # url_path="(?P<transaction_state>([all|inprogress|cancelled|abandoned|completed]){3,10})",
    @action(
        detail=False, methods=["get"], url_path="characters/(?P<id>[a-z0-9]+)/quotes"
    )
    def retrieve_character_quotes(self, request, **kwargs):
        """ Retrieves a character's quotes"""
        service_response = CharacterService.retrieve_character_quotes(
            user=request.user, character_id=kwargs["id"]
        )
        return ResponseManager.handle_response(
            message="Retrieval Success", data=service_response, status=200
        )
