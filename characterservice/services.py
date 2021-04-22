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
        cls,
        user: User = None,
        character_id: str = None,
        favorite_status_meta: Dict = None,
    ) -> Dict:

        # If we have favorited a character then the un-favorite them
        if favorite_status_meta.get("favorited") is True:
            Favorite.objects.filter(
                user=user,
                entry_id=character_id,
            ).update(is_favorite=False)
            return {"character_id": character_id, "favorite_status": False}

        # Else we make the call to retrieve their details and favorite them
        # If record exist we don't want to make a redundant call to get character details
        # This typically happens the third time the endpoint is hit
        response = None  # To prevent out of bound error
        if favorite_status_meta.get("is_record_exist") is False:
            response = OneAPIAdapter.retrieve_a_character(
                api_token=user.api_token, character_id=character_id
            )

        update_data = {
            "entry_type": "character",
            "entry_details": response["docs"][0] if response else response,
            "is_favorite": True,
        }

        # If the record exist we dont want to update this field
        if favorite_status_meta.get("is_record_exist") is True:
            del update_data["entry_details"]

        Favorite.objects.update_or_create(
            user=user, entry_id=character_id, defaults=update_data
        )

        return {"character_id": character_id, "favorite_status": True}

    @classmethod
    def favourite_a_character_quote(
        cls,
        user: User = None,
        quote_id: str = None,
        character_id: str = None,
        favorite_status_meta: Dict = None,
    ) -> Dict:

        # If we have favorited a character then the un-favorite them
        if favorite_status_meta.get("favorited") is True:
            Favorite.objects.filter(
                user=user,
                entry_id=quote_id,
            ).update(is_favorite=False)
            return {"quote_id": quote_id, "favorite_status": False}

        # Else we make the call to retrieve their details and favorite them
        response = None
        # If record exist we don't want to make a redundant call to get character details
        if favorite_status_meta.get("is_record_exist") is False:
            response = OneAPIAdapter.retrieve_a_quote(
                api_token=user.api_token, quote_id=quote_id
            )

        # Here we check that the quote belongs to the character
        if isinstance(response, dict) and len(response["docs"]):
            if character_id != response["docs"][0]["character"]:
                raise ValidationError(dict(error="Quote not found for this character"))

        update_data = {
            "entry_type": "quote",
            "entry_details": response["docs"][0] if response else response,
            "is_favorite": True,
        }

        # We remove entry details because it'd throw KeyError as call to the One API was done
        if favorite_status_meta.get("is_record_exist") is True:
            del update_data["entry_details"]

        Favorite.objects.update_or_create(
            user=user, entry_id=quote_id, defaults=update_data
        )

        return {"quote_id": quote_id, "favorite_status": True}
