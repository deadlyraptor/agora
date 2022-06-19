from django.urls import path

from agora.apps.stores import views

urlpatterns = [
    path('stores/',
         views.StoreListView.as_view(),
         name='store-list'),
    path('new/',
         views.StoreCreateView.as_view(),
         name='store-create'),
    path('<int:pk>/delete',
         views.StoreDeleteView.as_view(),
         name='store-delete')
]
