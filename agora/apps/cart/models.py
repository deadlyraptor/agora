from django.db import models

from agora.apps.products.models import Product
from agora.apps.users.models import User


class CartItem(models.Model):
    """A model for items in the shopping cart."""

    item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_item')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['item']

    def __repr__(self):
        return f'<CartItem(<item={self.item}, user={self.user})>'

    def __str__(self):
        return f'{self.item}'
