"""agora URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('agora.apps.core.urls')),
    path('products/', include('agora.apps.products.urls')),
    path('stores/', include('agora.apps.stores.urls')),
    path('tags/', include('agora.apps.tags.urls')),
    path('account/', include('agora.apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
