from django.http import Http404
from django.views.generic.detail import SingleObjectMixin

from agora.apps.products.models import Brand


class UserSingleBrandMixin(SingleObjectMixin):

    def get_object(self):
        try:
            return Brand.objects.get(pk=self.kwargs['pk'],
                                     store__user=self.request.user)
        except Brand.DoesNotExist:
            raise Http404('This brand does not exist.')
