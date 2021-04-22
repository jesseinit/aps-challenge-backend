from characterservice.models import Favorite
from typing import Dict
from userservice.models import User
from utils.helpers import OneAPIAdapter
from rest_framework.exceptions import (
    ValidationError,
    AuthenticationFailed,
    PermissionDenied,
)


class CharacterService:
    """ Service class that helps working with Character Resource """

    @classmethod
    def retrieve_characters(cls, user: User = None) -> Dict:
        response = OneAPIAdapter.retrieve_characters(api_token=user.api_token)
        return response["docs"]

    @classmethod
    def retrieve_character_quotes(
        cls, user: User = None, character_id: str = None
    ) -> Dict:
        response = OneAPIAdapter.retrieve_character_quotes(
            api_token=user.api_token, character_id=character_id
        )
        return response["docs"]

    @classmethod
    def favourite_a_character(
        cls, user: User = None, character_id: str = None, favorite_status: bool = False
    ) -> Dict:

        # If we have favorited a character then the un-favorite them
        if favorite_status is True:
            Favorite.objects.filter(
                user=user,
                entry_id=character_id,
            ).update(is_favorite=False)
            return {"character_id": character_id, "favorite_status": False}

        # Else we make the call to retrieve their details and favorite them
        response = OneAPIAdapter.retrieve_a_character(
            api_token=user.api_token, character_id=character_id
        )

        Favorite.objects.update_or_create(
            user=user,
            entry_id=character_id,
            defaults={
                "entry_type": "character",
                "entry_details": response["docs"][0],
                "is_favorite": True,
            },
        )
        return {"character_id": character_id, "favorite_status": True}
