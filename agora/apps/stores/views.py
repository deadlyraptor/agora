from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import CreateView

from agora.apps.stores.forms import StoreForm


class StoreCreateView(CreateView):
    """A view for creating new stores."""

    form_class = StoreForm
    success_url = reverse_lazy('store-create')
    template_name = 'stores/store_form.html'
