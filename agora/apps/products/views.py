from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from taggit.models import Tag, TaggedItem

from agora.apps.products.forms import ProductForm, BrandForm
from agora.apps.products.mixins import UserSingleBrandMixin
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
        return Product.objects.filter(brand__store__user=self.request.user)


class ProductCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new Products."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-create')
    success_message = '%(name)s (%(brand)s) successfully created.'
    template_name = 'products/product_form.html'
    extra_context = {'title': 'Create Product', 'button': 'Create'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProductDetailView(DetailView):
    """A view for inspecting a specific product."""

    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name})
        return super().get_context_data(**kwargs)

    def get_object(self):
        try:
            return Product.objects.get(pk=self.kwargs['pk'],
                                       brand__store__user=self.request.user)
        except Product.DoesNotExist:
            raise Http404('This product does not exist.')


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """A view for updating Products."""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')
    success_message = '%(name)s successfully updated.'
    template_name = 'products/product_form.html'
    extra_context = {'button': 'Update'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs.update({'title': f'Update {self.object.name}'})
        return super().get_context_data(**kwargs)

    def get_object(self):
        try:
            return Product.objects.get(pk=self.kwargs['pk'],
                                       brand__store__user=self.request.user)
        except Product.DoesNotExist:
            raise Http404('This product does not exist.')


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting Products."""

    model = Product
    success_url = reverse_lazy('product-list')
    success_message = 'Product successfully deleted.'
    template_name = 'products/product_confirm_delete.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': f'Delete {self.object.name}'})
        return super().get_context_data(**kwargs)

    def get_object(self):
        try:
            return Product.objects.get(pk=self.kwargs['pk'],
                                       brand__store__user=self.request.user)
        except Product.DoesNotExist:
            raise Http404('This product does not exist.')

# Brands


class BrandListView(ListView):
    """A view for listing all brands."""

    model = Brand
    context_object_name = 'brands'
    paginate_by = 25
    template_name = 'brand_list.html'
    extra_context = {'title': 'Brands'}

    def get_queryset(self):
        return Brand.objects.filter(store__user__pk=self.request.user.pk)


class BrandCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new brands."""

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('brand-create')
    success_message = '%(name)s successfully added to %(store)s.'
    template_name = 'products/brand_form.html'
    extra_context = {'title': 'Create Brand', 'button': 'Create'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BrandDetailView(UserSingleBrandMixin, DetailView):
    """A view for inspecting a specific brand."""

    model = Brand
    context_object_name = 'brand'
    template_name = 'products/brand_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name})
        return super().get_context_data(**kwargs)


class BrandUpdateView(SuccessMessageMixin, UserSingleBrandMixin, UpdateView):
    """A view for updating brands."""

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('brand-list')
    success_message = '%(name)s successfully updated.'
    template_name = 'products/brand_form.html'
    extra_context = {'button': 'Update'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs.update({'title': f'Update {self.object.name}'})
        return super().get_context_data(**kwargs)


class BrandDeleteView(SuccessMessageMixin, UserSingleBrandMixin, DeleteView):
    """A view for deleting brands."""

    model = Brand
    success_url = reverse_lazy('brand-list')
    success_message = 'Brand successfully deleted.'
    template_name = 'products/brand_confirm_delete.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': f'Delete {self.object.name}'})
        return super().get_context_data(**kwargs)


class TagListView(ListView):
    """A view for listing all tags."""

    model = Tag
    context_object_name = 'tags'
    paginate_by = 15
    template_name = 'products/tag_list.html'
    extra_context = {'title': 'Tags'}

    def get_queryset(self):
        return Tag.objects.all().order_by('name')


class TagDetailView(DetailView):
    """A view for inspecting a specific tag."""

    model = Tag
    context_object_name = 'tag'
    template_name = 'products/tag_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name.capitalize})
        kwargs.update({'products': TaggedItem.objects.filter(
            tag=self.object)})
        return super().get_context_data(**kwargs)


class TagDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting tags."""

    model = Tag
    success_url = reverse_lazy('tag-list')
    success_message = 'Tag succesfully deleted.'
    template_name = 'products/tag_confirm_delete.html'
    extra_context = {'title': 'Delete Tag'}
