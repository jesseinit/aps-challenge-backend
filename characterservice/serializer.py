from django.db.models import fields
from characterservice.models import Favorite
from utils.helpers import FieldValidators
from rest_framework import serializers


class FavoriteCharacterSerializer(serializers.Serializer):
    character_id = serializers.CharField()

    def validate_character_id(self, character_id):
        fav_instance = Favorite.objects.filter(
            user=self.context["user"], entry_id=character_id, entry_type="character"
        ).first()

        if fav_instance and fav_instance.is_favorite is True:
            self.fav_status = {"favorited": True}
            return character_id

        self.fav_status = {
            "favorited": False,
            "is_record_exist": True if fav_instance else False,
        }

        return character_id

    def to_representation(self, instance):
        """ Pass custom values to validation results """
        result = super().to_representation(instance)
        result["fav_status"] = self.fav_status
        return result


class MyFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteCharacterQuoteSerializer(serializers.Serializer):
    character_id = serializers.CharField(min_length=1)
    quote_id = serializers.CharField(min_length=1)

    def validate_quote_id(self, quote_id):
        fav_instance = Favorite.objects.filter(
            user=self.context["user"], entry_id=quote_id, entry_type="quote"
        ).first()

        if fav_instance and fav_instance.is_favorite is True:
            self.fav_status = {"favorited": True}
            return quote_id

        self.fav_status = {
            "favorited": False,
            "is_record_exist": True if fav_instance else False,
        }

        return quote_id

    def to_representation(self, instance):
        """ Pass custom values to validation results """
        result = super().to_representation(instance)
        result["fav_status"] = self.fav_status
        return result
