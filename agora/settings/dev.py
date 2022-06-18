from agora.settings.base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ['debug_toolbar']  # noqa

MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ['127.0.0.1']

try:
    from .local import *  # noqa
except ImportError:
    pass
