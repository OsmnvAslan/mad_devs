# TODO: always check for "python manage.py check --deploy"
from datetime import timedelta
from os.path import dirname, abspath, join

import sentry_sdk
from corsheaders.defaults import default_methods, default_headers
from environ import Env
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from .helpers import (
    DEFAULT_APPS, DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES,
    DEFAULT_MIDDLEWARE, REST_FRAMEWORK_SETTINGS, STORAGES,
    DEFAULT_STORAGE, DEFAULT_TEMPLATES, DEFAULT_VALIDATORS,
)

BASE_DIR = dirname(dirname(abspath(__file__)))

# Environment variables
env = Env()
Env.read_env()

# Sentry
SENTRY_DSN = env.str(var='SENTRY_DSN')
sentry_sdk.init(
    dsn=SENTRY_DSN, integrations=(DjangoIntegration(), CeleryIntegration())
)

# Django
DEBUG = env.bool(var='DEBUG')
SECRET_KEY = env.str(var='SECRET_KEY')
APPEND_SLASH = True
ALLOWED_HOSTS = ('*',)
INSTALLED_APPS = DEFAULT_APPS
MIDDLEWARE = DEFAULT_MIDDLEWARE
ROOT_URLCONF = 'core.urls'
TEMPLATES = DEFAULT_TEMPLATES
WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'
DATABASES = {
    'default': env.db()
}
AUTH_PASSWORD_VALIDATORS = DEFAULT_VALIDATORS
AUTH_USER_MODEL = 'common.ExtendedUser'

# Security
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = False

# Localization
LOCALE_PATHS = DEFAULT_LOCALE_PATHS
LANGUAGES = DEFAULT_LANGUAGES
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
TIME_ZONE = env.str(var='TIME_ZONE')
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# CorsHeaders
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = default_headers
CORS_ALLOW_CREDENTIALS = True

# Rest framework
REST_FRAMEWORK = REST_FRAMEWORK_SETTINGS

# Storage
DEFAULT_FILE_STORAGE = STORAGES.get(
    env.str(var='WHERE_TO_KEEP_MEDIA'), DEFAULT_STORAGE
)

# JWT
ALGORITHM = 'HS256'
EXPIRATION_TIME = timedelta(minutes=15)
