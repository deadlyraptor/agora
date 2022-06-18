"""agora URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agora.apps.core.urls')),
    path('store/', include('agora.apps.stores.urls')),
    path('account/', include('agora.apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
