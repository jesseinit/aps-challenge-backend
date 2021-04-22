from typing import Dict
from userservice.models import User
from utils.helpers import OneAPIAdapter


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
