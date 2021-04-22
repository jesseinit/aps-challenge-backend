# Create your views here.
from decimal import Context
import requests
from characterservice.services import CharacterService
from utils.helpers import ResponseManager

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from characterservice.serializer import (
    FavoriteCharacterSerializer,
    MyFavoritesSerializer,
)


class CharacterViewset(viewsets.ViewSet):
    @action(detail=False, methods=["get"], url_path="characters")
    def retrieve_characters(self, request):
        """ Retrieves all characters """
        service_response = CharacterService.retrieve_characters(user=request.user)
        return ResponseManager.handle_response(
            message="Retrieval Success", data=service_response, status=200
        )

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

    @action(
        detail=False, methods=["post"], url_path="characters/(?P<id>[a-z0-9]+)/favorite"
    )
    def favorite_character(self, request, **kwargs):
        """ Favorite a character"""
        serialized_data = FavoriteCharacterSerializer(
            data={"character_id": kwargs["id"]}, context={"user": request.user}
        )
        if not serialized_data.is_valid():
            return ResponseManager.handle_response(
                error=serialized_data.errors, status=400
            )

        service_response = CharacterService.favourite_a_character(
            user=request.user,
            character_id=kwargs["id"],
            favorite_status=serialized_data.data["is_character_favorited"],
        )

        return ResponseManager.handle_response(
            message="Success", data=service_response, status=200
        )

    @action(detail=False, methods=["get"], url_path="favorites")
    def retrieve_favorites(self, request):
        """ Retrieve my favorites"""
        serialized_data = MyFavoritesSerializer(
            request.user.favorite_characters.filter(is_favorite=True), many=True
        )
        return ResponseManager.handle_response(
            message="Success", data=serialized_data.data, status=200
        )
