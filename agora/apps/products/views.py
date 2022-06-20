from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from taggit.models import Tag

from agora.apps.products.forms import ProductForm, BrandForm
from agora.apps.products.models import Product, Brand

# Products


class ProductListView(ListView):
    """A view for listing all products."""

    model = Product
    context_object_name = 'products'
    paginate_by = 15
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


class ProductDetailView(DetailView):
    """A view for inspecting a specific product."""

    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name})
        return super().get_context_data(**kwargs)


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
    success_message = '%(name)s successfully added to %(store)s.'
    template_name = 'products/brand_form.html'
    extra_context = {'title': 'Create Brand', 'button': 'Create'}


class BrandDetailView(DetailView):
    """A view for inspecting a specific brand."""

    model = Brand
    context_object_name = 'brand'
    template_name = 'products/brand_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name})
        return super().get_context_data(**kwargs)


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


class TagListView(ListView):
    """A view for listing all tags."""

    model = Tag
    context_object_name = 'tags'
    paginate_by = 15
    template_name = 'products/tag_list.html'
    extra_context = {'title': 'Tags'}

    def get_queryset(self):
        return Tag.objects.all().order_by('name')


class TagDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting tags."""

    model = Tag
    success_url = reverse_lazy('tag-list')
    success_message = 'Tag succesfully deleted.'
    template_name = 'products/tag_confirm_delete.html'
    extra_context = {'title': 'Delete Tag'}
