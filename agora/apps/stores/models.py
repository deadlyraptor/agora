from django.db import models

from model_utils.models import TimeStampedModel


class Store(TimeStampedModel, models.Model):
    """A model for grocery stores."""

    name = models.CharField(max_length=150)
    website = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
