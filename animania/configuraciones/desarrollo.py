from .base import *
from .basesdatos import NOMBREDB_DESARROLLO

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR.child(NOMBREDB_DESARROLLO),
	}
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
