from django.db.models import fields
from characterservice.models import Favorite
from utils.helpers import FieldValidators
from rest_framework import serializers


class FavoriteCharacterSerializer(serializers.Serializer):
    character_id = serializers.CharField()

    def validate_character_id(self, character_id):
        fav_character = Favorite.objects.filter(
            user=self.context["user"], entry_id=character_id
        ).first()

        if fav_character and fav_character.is_favorite is True:
            self.is_character_favorited = True
            return character_id

        self.is_character_favorited = False
        return character_id

    def to_representation(self, instance):
        """ Pass customer values to validation results """
        result = super().to_representation(instance)
        result["is_character_favorited"] = self.is_character_favorited
        return result


class MyFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
