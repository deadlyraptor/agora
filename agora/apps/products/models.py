from django.core.validators import MinValueValidator
from django.db import models

from model_utils.models import TimeStampedModel
from quantityfield.fields import QuantityField
from taggit.managers import TaggableManager

from agora.apps.stores.models import Store


class Product(TimeStampedModel, models.Model):
    """A model for grocery store products."""

    name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0)]
    )
    promo_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0.00,
        validators=[MinValueValidator(0)]
    )
    weight = QuantityField('ounce',
                           validators=[MinValueValidator(0)])
    brand = models.ForeignKey(
        'ProductBrand',
        on_delete=models.CASCADE,
        related_name='products'
    )
    notes = models.TextField(blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.store})'


class ProductBrand(TimeStampedModel, models.Model):
    """A model for product brands."""

    name = models.CharField(max_length=50)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='brands'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.store})'
