from django.urls import path

from agora.apps.products import views

urlpatterns = [
    # Products
    path('products/',
         views.ProductListView.as_view(),
         name='product-list'),
    path('new/',
         views.ProductCreateView.as_view(),
         name='product-create'),
    path('<int:pk>/edit/',
         views.ProductUpdateView.as_view(),
         name='product-update'),
    path('<int:pk>/delete/',
         views.ProductDeleteView.as_view(),
         name='product-delete'),
    # Brands
    path('brands/',
         views.BrandListView.as_view(),
         name='brand-list'),
    path('brand/new/',
         views.BrandCreateView.as_view(),
         name='brand-create'),
    path('<int:pk>/edit',
         views.BrandUpdateView.as_view(),
         name='brand-update'),
]
