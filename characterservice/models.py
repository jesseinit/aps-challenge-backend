# Create your models here.
from utils.model_helpers import BaseAbstractModel
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.
class Favorite(BaseAbstractModel):
    """ Favorites Model """

    ENTRY_TYPE = [("character", "character"), ("quote", "quote")]

    class Meta:
        db_table = "Favorite"

    user = models.ForeignKey(
        "userservice.User", on_delete=models.CASCADE, related_name="favorite_characters"
    )
    entry_id = models.CharField(max_length=50)
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE)
    entry_details = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    is_favorite = models.BooleanField(default=True)

    def __str__(self):
        return f"FavoriteCharacter >>> {self.entry_id}"

    def __repr__(self):
        return f"FavoriteCharacter >>> {self.entry_id}"
