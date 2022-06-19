from django.urls import path

from agora.apps.products import views

urlpatterns = [
    path('new/',
         views.ProductCreateView.as_view(),
         name='product-create'),
]
