

from pathlib import Path
import globals
import os
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kyn!@lrtv)xppnc*mur&15p#ai)bhtrtb8#tg13k+pl+pjcftz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'core',
    'main',
    'durationwidget',
    'drf_spectacular',
    'test_log.apps.TestLogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = f'{globals.PROJECT_NAME}.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

WSGI_APPLICATION = f'{globals.PROJECT_NAME}.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:3000',
)


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='psql://admin:ooprojectpass@127.0.0.1:5432/ooproject'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# swagger

SPECTACULAR_SETTINGS = {
    'TITLE': 'ooproject API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# djoser


DJOSER = {

    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'main.serializers.CustomUserCreateSerializer',
        'user': 'main.serializers.CustomUserSerializer',
        'user_update': 'djoser.serializers.UserUpdateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'current_user': 'main.serializers.CustomUserSerializer',
    },
}

DOMAIN = 'localhost:3000'
SITE_NAME = 'localhost:3000'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# redis caching

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis'
    }
}
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.User'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = globals.EMAIL
EMAIL_HOST_PASSWORD = globals.PASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

LOGGING = {
 'version': 1,
 'disable_existing_loggers': False,
 'formatters': {
  'simple': {
   'format': '[%(asctime)s] %(levelname)s | %(funcName)s | %(name)s | %(message)s',
   'datefmt': '%Y-%m-%d %H:%M:%S',
  },
 },
 'handlers': {
  'logger': {
   'level': 'DEBUG',
   'class': 'logging.handlers.RotatingFileHandler',
   'filename': BASE_DIR + '/logs/test.log',
   'formatter': 'simple',
  }
 },
 'loggers': {
  'signal': {
   'handlers': ['logger'],
   'level': 'DEBUG',
  }
 }
}