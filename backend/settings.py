"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from datetime import timedelta

import environ
from corsheaders.defaults import default_headers, default_methods

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Path helper
def location(x):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)


if os.environ.get('ENV') != 'PRODUCTION' and not os.environ.get('IS_DOCKER'):
    # Take environment variables from local.env file
    # if not production mode and not in docker
    environ.Env.read_env(location('./.env_file/local/.local.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')
else:
    DEBUG = True
    SECRET_KEY = 'fqBz9>xB:1\x0b:=e*S3&Df*rO#f=Ldu<x$0tXbnk]N9m,b7xgumQ'

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with
# a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party librairie
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',
    'django_extensions',

    # local
    'api',  # endpoint app
    'student',  # app to manage students issue.
    'users',  # app to manage users
]

AUTH_USER_MODEL = 'users.UserAccount'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 3rd
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if os.environ.get('ENV') != 'PRODUCTION':
    MIDDLEWARE += [
        'django_pdb.middleware.PdbMiddleware',
    ]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE'),
        'NAME': os.environ.get('SQL_DB'),
        'USER': os.environ.get('SQL_USER'),
        'PASSWORD': os.environ.get('SQL_PASSWORD'),
        'HOST': os.environ.get('SQL_HOST'),
        'PORT': os.environ.get('SQL_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

# Store this str to v_, because it is too long
v_ = 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': v_
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Africa/Casablanca'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = '/static/'
STATIC_ROOT = location('static')

# MEDIA SETTINGS
MEDIA_URL = '/media/'
MEDIA_ROOT = location('media/')

# Static files css for production

if os.environ.get('ENV') == 'PRODUCTION':
    """ Sometimes Django apps are deployed at a particular prefix
    (or “subdirectory”) on a domain e.g. http://example.com/my-app/ rather than
    just http://example.com. In this case you would normally use Django’s
    FORCE_SCRIPT_NAME setting to tell the application where it is located
    """
    # FORCE_SCRIPT_NAME = '/blog'
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    STATIC_ROOT = location('staticfiles')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = location('mediafiles')

    ADMIN_MEDIA_PREFIX = 'media'

    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

# api configuration

# Disable browsable api in production
DEFAULT_RENDERER_CLASSES = ('rest_framework.renderers.JSONRenderer', )

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        'rest_framework.renderers.BrowsableAPIRenderer', )

# REST framwork configuration
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS':
    ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        #  'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        "rest_framework.authentication.SessionAuthentication",
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES':
    DEFAULT_RENDERER_CLASSES,
    'TEST_REQUEST_DEFAULT_FORMAT':
    'json',
}

# Configuration for dj_rest_auth
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'jwt-auth'

# SIMPLE_JWT configuration
SIMPLE_JWT = {
    'JWT_ALLOW_REFRESH': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_HEADER_TYPES': (
        'Bearer',
        'Token',
        'JWT',
    ),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}

DJOSER = {
    "SERIALIZERS": {
        "user_create": "api.serializers.users.UserCreateSerializer",
        "user": "api.serializers.users.UserSerializer",
        "current_user": "api.serializers.users.UserSerializer",
    },
    "LOGIN_FIELD": "email",
    "PASSWORD_RESET_CONFIRM_URL": "auth/password/reset/{uid}/{token}",
}

# CORS HEADERS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:1337",  # for nginx server
    "http://localhost:80",  # for nginx server
    "http://localhost:8000",  # for django itself
]

if os.environ.get('ENV') != 'PRODUCTION':
    CORS_ALLOWED_ORIGINS.append("http://localhost:3000")  # react
    CORS_ALLOWED_ORIGINS.append("http://127.0.0.1:8080")  # vuejs
    CORS_ALLOWED_ORIGINS.append("http://192.168.11.106:8080")  # vuejs
    CORS_ALLOWED_ORIGINS.append("http://localhost:8080")  # vuejs

# allows http verbs

CORS_ALLOW_METHODS = list(default_methods) + [
    #  "POKE",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Amz-Date',  # to make nginx for work
]

# Configuration for django resize
DJANGORESIZED_DEFAULT_SIZE = [400, 240]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg", 'PNG': ".png"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

# CKEditor Settings
CKEDITOR_BASEPATH = location("/static/ckeditor/ckeditor/")
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'upload/')
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',
        'extraPlugins': ','.join(['codesnippet', 'youtube']),
    },
}

# Account Settings
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/author/dashboard/'
LOGOUT_REDIRECT_URL = '/account/logout/'

# Email Settings (Development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if os.environ.get('ENV') == 'PRODUCTION':
    # Email Settings (Production)
    EMAIL_BACKEND = ''
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ""
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Celery stuff configutation
#  BROKER_URL = 'redis://localhost:6379'
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Casablanca'
