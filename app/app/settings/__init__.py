import os

# development environment by default
if os.environ['DJANGO_SETTINGS_MODULE'] == 'app.settings':
    from .development import *
