from django.urls import path

from agora.apps.stores import views

urlpatterns = [
    path('new/',
         views.StoreCreateView.as_view(),
         name='store-create'),
]
