from utils.model_helpers import BaseAbstractModel
from django.db import models

# Create your models here.
class User(BaseAbstractModel):
    """ User Model """

    class Meta:
        db_table = "User"

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    api_token = models.CharField(max_length=100, null=True, default=None)

    def __str__(self):
        return f"User >>> {self.email}"

    def __repr__(self):
        return f"User >>> {self.email}"
