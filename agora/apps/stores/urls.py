from django.urls import path

from agora.apps.stores import views

urlpatterns = [
    path('',
         views.StoreListView.as_view(),
         name='store-list'),
    path('new/',
         views.StoreCreateView.as_view(),
         name='store-create'),
    path('<int:pk>',
         views.StoreDetailView.as_view(),
         name='store-detail'),
    path('<int:pk>/edit',
         views.StoreUpdateView.as_view(),
         name='store-update'),
    path('<int:pk>/delete',
         views.StoreDeleteView.as_view(),
         name='store-delete')
]
