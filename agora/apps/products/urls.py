from django.urls import path

from agora.apps.products import views

urlpatterns = [
    path('products/',
         views.ProductListView.as_view(),
         name='product-list'),
    path('new/',
         views.ProductCreateView.as_view(),
         name='product-create'),
]
