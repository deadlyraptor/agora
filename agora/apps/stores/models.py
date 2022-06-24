from django.db import models

from model_utils.models import TimeStampedModel

from agora.apps.users.models import User


class Store(TimeStampedModel, models.Model):
    """A model for grocery stores."""

    name = models.CharField(max_length=150)
    website = models.URLField()
    directions = models.URLField()
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='stores')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
