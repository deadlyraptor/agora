from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from agora.apps.cart.forms import CartItemForm
from agora.apps.cart.models import CartItem
from agora.apps.products.models import Product


class CartListView(ListView):
    """A view for inspecting the shopping cart."""

    model = CartItem
    context_object_name = 'items'
    template_name = 'cart/cart_list.html'
    extra_context = {'title': 'Shopping List'}

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CartItemCreateView(SuccessMessageMixin, CreateView):
    """A view for adding an item to the shopping list."""

    model = CartItem
    form_class = CartItemForm
    success_url = reverse_lazy('product-list')
    success_message = '%(item)s added to shopping list.'
    template_name = 'cart/cart_item_form.html'
    extra_context = {'title': 'Add Item'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['item'] = Product.objects.get(pk=self.kwargs['pk'])
        kwargs['user'] = self.request.user
        return kwargs


class CartItemDeleteView(SuccessMessageMixin, DeleteView):
    """A view for removing an item from the shopping list."""

    model = CartItem
    success_url = reverse_lazy('cart')
    success_message = 'Item removed from cart.'
    template_name = 'cart/item_confirm_delete.html'
    extra_context = {'title': 'Remove Item'}
