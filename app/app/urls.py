from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Add app urls here
]

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns += [path('admin/', admin.site.urls)]

if settings.SERVE_MEDIA:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
