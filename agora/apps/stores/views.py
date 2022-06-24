from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from agora.apps.stores.forms import StoreForm
from agora.apps.stores.models import Store


class StoreListView(ListView):
    """A view for listing all stores."""

    model = Store
    context_object_name = 'stores'
    paginate_by = 25
    template_name = 'stores/store_list.html'
    extra_context = {'title': 'Stores'}

    def get_queryset(self):
        return Store.objects.all()


class StoreCreateView(SuccessMessageMixin, CreateView):
    """A view for creating new stores."""

    form_class = StoreForm
    success_url = reverse_lazy('store-create')
    success_message = '%(name)s successfully created.'
    template_name = 'stores/store_form.html'
    extra_context = {'title': 'Create Store', 'button': 'Create'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class StoreDetailView(DetailView):
    """A view for inspecting a specific store."""

    model = Store
    context_object_name = 'store'
    template_name = 'stores/store_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'title': self.object.name})
        return super().get_context_data(**kwargs)


class StoreUpdateView(SuccessMessageMixin, UpdateView):
    """A view for updating stores."""

    model = Store
    form_class = StoreForm
    success_url = reverse_lazy('store-list')
    success_message = '%(name)s successfully updated.'
    template_name = 'stores/store_form.html'
    extra_context = {'title': 'Update Store', 'button': 'Update'}


class StoreDeleteView(SuccessMessageMixin, DeleteView):
    """A view for deleting stores."""

    model = Store
    success_url = reverse_lazy('store-list')
    success_message = 'Store successfully deleted.'
    template_name = 'stores/store_confirm_delete.html'
    extra_context = {'title': 'Delete Store'}
