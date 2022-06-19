from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from agora.apps.products.forms import ProductForm
from agora.apps.products.models import Product


class ProductCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new Products."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-create')
    success_message = '%(name)s added to %(store)s successfully.'
    template_name = 'products/product_form.html'
    extra_context = {'title': 'Create Product'}
