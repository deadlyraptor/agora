from datetime import datetime

from django import forms

from agora.apps.products.models import Product, Brand


class ProductForm(forms.ModelForm):
    """A form for creating and updating Products."""

    class Meta:
        model = Product
        exclude = ('created', 'modified')
        widgets = {
            'purchase_date': forms.TextInput(attrs={
                'max': datetime.today().strftime('%Y-%m-%d')})
        }


class BrandForm(forms.ModelForm):
    """A form for creating and updating product brands."""

    class Meta:
        model = Brand
        exclude = ('exclude', 'modified')
