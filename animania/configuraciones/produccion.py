from .base import *
from .basesdatossproyecto import (
    TIPODB_PRODUCCION,
    NOMBREDB_PRODUCCION,
    USUARIO_PRODUCCION,
    CONTRASENIA_PRODUCCION,
    IP_PRODUCCION,
    PUERTO_PRODUCCION,
)

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': TIPODB_PRODUCCION,
        'NAME': NOMBREDB_PRODUCCION,
        'USER': USUARIO_PRODUCCION,
        'PASSWORD': CONTRASENIA_PRODUCCION,
        'HOST': IP_PRODUCCION,
        'PORT': PUERTO_PRODUCCION,
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
