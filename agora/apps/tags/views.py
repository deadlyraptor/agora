from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from taggit.models import Tag, TaggedItem


class TagListView(ListView):
    """A view for listing all tags."""

    model = Tag
    context_object_name = 'tags'
    paginate_by = 15
    template_name = 'tags/tag_list.html'
    extra_context = {'title': 'Tags'}

    def get_queryset(self):
        return Tag.objects.filter(
            product__brand__store__user=self.request.user).order_by('name')


class TagDetailView(DetailView):
    """A view for inspecting a specific tag."""

    model = Tag
    context_object_name = 'tag'
    template_name = 'tags/tag_detail.html'

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
    template_name = 'tags/tag_confirm_delete.html'
    extra_context = {'title': 'Delete Tag'}
