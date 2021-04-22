from django.db import models
import uuid


class BaseAbstractModel(models.Model):
    """ Base Abstract Model """

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    id = models.CharField(
        max_length=60,
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update(self, **kwargs):
        if self._state.adding:
            raise self.DoesNotExist
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save(update_fields=kwargs.keys())
        return self
