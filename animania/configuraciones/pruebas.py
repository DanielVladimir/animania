from .base import *
from .basesdatossproyecto import (
    TIPODB_PRUEBAS,
    NOMBREDB_PRUEBAS,
    USUARIO_PRUEBAS,
    CONTRASENIA_PRUEBAS,
    IP_PRUEBAS,
    PUERTO_PRUEBAS
)

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': TIPODB_PRUEBAS,
        'NAME': NOMBREDB_PRUEBAS,
        'USER': USUARIO_PRUEBAS,
        'PASSWORD': CONTRASENIA_PRUEBAS,
        'HOST': IP_PRUEBAS,
        'PORT': PUERTO_PRUEBAS,
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
