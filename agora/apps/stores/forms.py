from django import forms

from agora.apps.stores.models import Store


class StoreForm(forms.ModelForm):
    """A form for creating and updating Stores."""

    class Meta:
        model = Store
        exclude = ('created', 'modified')
