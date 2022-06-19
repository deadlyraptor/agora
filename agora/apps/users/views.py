from django.views.generic import DetailView

from agora.apps.users.models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
