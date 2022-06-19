from django.urls import path

from agora.apps.users import views

urlpatterns = [
    path('<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]
