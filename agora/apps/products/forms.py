from django import forms

from agora.apps.products.models import Product, ProductBrand


class ProductForm(forms.ModelForm):
    """A form for creating and updating Products."""

    class Meta:
        model = Product
        exclude = ('created', 'modified')


class ProductBrandForm(forms.ModelForm):
    """A form for creating and updating product brands."""

    class Meta:
        model = ProductBrand
        exclude = ('exclude', 'modified')
