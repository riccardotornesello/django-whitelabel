import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
ADMIN_ENABLED = True
if ADMIN_ENABLED:
    INSTALLED_APPS.append('django.contrib.admin')

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
CORS_ALLOWED_ORIGINS = os.environ['CORS_ALLOWED_ORIGINS'].split(',')
CSRF_TRUSTED_ORIGINS = os.environ['CSRF_TRUSTED_ORIGINS'].split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'database',
        'PORT': '3306',
        'NAME': 'app_db',
        'USER': 'app_db',
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
    }
}

SERVE_MEDIA = False
