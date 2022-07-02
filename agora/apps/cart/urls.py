from django.urls import path

from agora.apps.cart import views

urlpatterns = [
    path('',
         views.CartListView.as_view(),
         name='cart'),
    path('add-to-list/<int:pk>/',
         views.CartItemCreateView.as_view(),
         name='add-to-list'),
    path('remove-from-list/<int:pk>/',
         views.CartItemDeleteView.as_view(),
         name='remove-from-list'),
]
