"""
WSGI config for animania project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animania.configuraciones.desarrollo")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animania.configuraciones.pruebas")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animania.configuraciones.produccion")

application = get_wsgi_application()
