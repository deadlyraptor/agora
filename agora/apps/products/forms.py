from django import forms

from agora.apps.products.models import Product


class ProductForm(forms.ModelForm):
    """A form for creating and updating Products."""

    class Meta:
        model = Product
        exclude = ('created', 'modified')
