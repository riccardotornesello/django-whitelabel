import os
from .base import *

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-$)2_c-h_%*e#7uk-eeq*@)=^toz2_1(yydewx2up+3mysi%9w%'
)

DEBUG = True
ADMIN_ENABLED = True
if ADMIN_ENABLED:
    INSTALLED_APPS.append('django.contrib.admin')

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']

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

SERVE_MEDIA = True
