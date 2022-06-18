from django.urls import path

from agora.apps.core import views

urlpatterns = [
    path('', views.index, name='index'),
]
