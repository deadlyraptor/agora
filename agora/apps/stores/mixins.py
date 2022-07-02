from django.http import Http404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from agora.apps.stores.models import Store


class UserMultipleStoreMixin(MultipleObjectMixin):

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user)


class UserSingleStoreMixin(SingleObjectMixin):

    def get_object(self):
        try:
            return Store.objects.get(pk=self.kwargs['pk'],
                                     user=self.request.user)
        except Store.DoesNotExist:
            raise Http404('This store does not exist.')
