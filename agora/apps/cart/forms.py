from django import forms

from agora.apps.cart.models import CartItem


class CartItemForm(forms.ModelForm):
    """A form for creating a CartItem."""

    class Meta:
        model = CartItem
        fields = ('item', 'user')

    def __init__(self, item, user, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        self.fields['item'].initial = item
        self.fields['user'].initial = user
