from django.urls import path

from agora.apps.products import views

urlpatterns = [
    # Products
    path('',
         views.ProductListView.as_view(),
         name='product-list'),
    path('new/',
         views.ProductCreateView.as_view(),
         name='product-create'),
    path('product/<int:pk>/',
         views.ProductDetailView.as_view(),
         name='product-detail'),
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
    path('brands/new/',
         views.BrandCreateView.as_view(),
         name='brand-create'),
    path('brand/<int:pk>/',
         views.BrandDetailView.as_view(),
         name='brand-detail'),
    path('brand/<int:pk>/edit/',
         views.BrandUpdateView.as_view(),
         name='brand-update'),
    path('brand/<int:pk>/delete/',
         views.BrandDeleteView.as_view(),
         name='brand-delete'),
]
