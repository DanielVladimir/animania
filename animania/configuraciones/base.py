#encoding:utf-8
from unipath import Path
from .llavesproyecto import LLAVESECRETA

BASE_DIR = Path(__file__).ancestor(3)
ADMINS = ('Daniel Vladimir', 'animaniastudio@gmail.com')
SECRET_KEY = LLAVESECRETA


### DEFINICION DE APLICACIONES ###
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TERCEROS_APPS = [
	'flat',
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
	#'',
]

INSTALLED_APPS = DJANGO_APPS + TERCEROS_APPS + LOCAL_APPS


### DEFINICION DE MIDDLEWARE ###
DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TERCEROS_MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

LOCAL_MIDDLEWARE = [
	#'',
]

MIDDLEWARE = DJANGO_MIDDLEWARE + TERCEROS_MIDDLEWARE + LOCAL_MIDDLEWARE


ROOT_URLCONF = 'animania.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'animania.wsgi.application'


### VALIDACION DE CONTRASEÑA ###
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


### INTERNACIONALIZACION ###
LANGUAGE_CODE = 'es-MX'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True


### API REST ###
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}


### CORS ORIGINS ###
CORS_ORIGIN_ALLOW_ALL = True
