from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from agora.apps.products.forms import ProductForm, ProductBrandForm
from agora.apps.products.models import Product, ProductBrand


class ProductListView(ListView):
    """A view for listing all products."""

    model = Product
    context_object_name = 'products'
    paginate_by = 25
    template_name = 'products/product_list.html'
    extra_context = {'title': 'Products'}

    def get_queryset(self):
        return Product.objects.all()


class ProductCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new Products."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-create')
    success_message = '%(name)s (%(brand)s) successfully created.'
    template_name = 'products/product_form.html'
    extra_context = {'title': 'Create Product', 'button': 'Create'}


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """A view for updating Products."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')
    success_message = '%(name)s successfully updated.'
    template_name = 'products/product_form.html'
    extra_context = {'title': 'Update Product', 'button': 'Update'}


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting Products."""

    model = Product
    success_url = reverse_lazy('product-list')
    success_message = 'Product successfully deleted.'
    template_name = 'products/product_confirm_delete.html'
    extra_context = {'title': 'Delete Product'}


class ProductBrandCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new product brands."""

    model = ProductBrand
    form_class = ProductBrandForm
    success_url = reverse_lazy('product-brand-create')
    success_message = '%(name)s added to %(store)s successfully.'
    template_name = 'products/product_brand_form.html'
    extra_context = {'title': 'Create Brand'}
