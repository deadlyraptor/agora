from agora.settings.base import *  # noqa
import dj_database_url

ALLOWED_HOSTS = [os.getenv('DOMAIN_NAME')]  # noqa
DATABASES['default'] = dj_database_url.config()  # noqa

try:
    from .local import *  # noqa
except ImportError:
    pass
