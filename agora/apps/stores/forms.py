from django import forms

from agora.apps.stores.models import Store


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        exclude = ('created', 'modified')
