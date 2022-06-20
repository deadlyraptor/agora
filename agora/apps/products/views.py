from ast import Delete
from audioop import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from agora.apps.products.forms import ProductForm, BrandForm
from agora.apps.products.models import Product, Brand

# Products


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


# Brands
class BrandListView(ListView):
    """A view for listing all brands."""

    model = Brand
    context_object_name = 'brands'
    paginate_by = 25
    template_name = 'brand_list.html'
    extra_context = {'title': 'Brands'}

    def get_queryset(self):
        return Brand.objects.all()


class BrandCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new brands."""

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('brand-create')
    success_message = '%(name)s added to %(store)s successfully.'
    template_name = 'products/brand_form.html'
    extra_context = {'title': 'Create Brand', 'button': 'Create'}


class BrandUpdateView(SuccessMessageMixin, UpdateView):
    """A view for updating brands."""

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('brand-list')
    success_message = '%(name)s successfully updated.'
    template_name = 'products/brand_form.html'
    extra_context = {'title': 'Update Brand', 'button': 'Update'}


class BrandDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting brands."""

    model = Brand
    success_url = reverse_lazy('brand-list')
    success_message = 'Brand successfully deleted.'
    template_name = 'products/brand_confirm_delete.html'
    extra_context = {'title': 'Delete Brand'}
