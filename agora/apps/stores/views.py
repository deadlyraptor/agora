from typing import List
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from agora.apps.stores.forms import StoreForm
from agora.apps.stores.models import Store


class StoreListView(ListView):
    """A view for listing all stores."""

    model = Store
    context_object_name = 'stores'
    template_name = 'stores/store_list.html'
    paginate_by = 25
    extra_context = {'title': 'Stores'}

    def get_queryset(self):
        return Store.objects.all()


class StoreCreateView(CreateView):
    """A view for creating new stores."""

    form_class = StoreForm
    success_url = reverse_lazy('store-create')
    template_name = 'stores/store_form.html'
    extra_context = {'title': 'Create Store'}
