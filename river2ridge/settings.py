"""
Django settings for site project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

"""


import os
# from social_core.pipeline.social_auth import social_user
# from social_core.pipeline.user import get_username
import dj_database_url

# ============================================================================
# Main Django Settings
# ============================================================================

db_from_env = dj_database_url.config()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Set the below in .env
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'river2ridge-site.herokuapp.com',
    'river2ridge-staging.herokuapp.com',
    'localhost',
]

# Application definition

R2R_APPS = [
    'apps.core',
    'apps.user',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = [
    'social_django',
    'django_extensions',
    'rest_framework',
    'djcelery',
]

INSTALLED_APPS += DJANGO_APPS
INSTALLED_APPS += R2R_APPS

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'river2ridge.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.csrf',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'river2ridge.wsgi.application'

# ============================================================================
# Databases
# ============================================================================

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DATABASES['default'].update(db_from_env)

# ============================================================================
# Authentication
# ============================================================================

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.steam.SteamOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

# # ============================================================================
# # Social Auth
# # ============================================================================
#
# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.social_user',
#     # 'social_core.pipeline.user.get_username',
#     'apps.user.pipeline.get_username',
#     'social_core.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
#     'social_core.pipeline.social_auth.associate_by_email',
#     # If there already is an account with the given steamid, pass it on to the pipeline
#     'apps.user.pipeline.associate_existing_user',
#     # The username for the account is always the steamid
#     # 'social_core.pipeline.user.get_username', # Function to get the username was changed
#     # Update the user record with any changed info from the auth service.
#     # 'social_core.pipeline.user.user_details',
#     # Use a custom function for this, since the details are provided separately
#     'apps.user.pipeline.user_details',
# )
#
# # User model settings
#
# AUTH_USER_MODEL = 'user.SteamUser'
# SOCIAL_AUTH_USER_MODEL = 'user.SteamUser'
#
# # Set the below line in .env
# SOCIAL_AUTH_STEAM_API_KEY = os.environ.get('API_KEY')
#
# # Social auth extra details
# SOCIAL_AUTH_STEAM_EXTRA_DATA = ['player']
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
# # SOCIAL_AUTH_STEAM_USER_FIELDS = ('username', 'email', 'steamid', 'date_joined')
#
# # ============================================================================
# # Custom Groups TODO: Make useful
# # ============================================================================
#
# ULX_ADMIN_RANKS = ['admin']
# ULX_SUPER_RANKS = ['developer', 'owner', 'co-owner', 'superadmin']
#
# # CSRF_TRUSTED_ORIGINS = []

# ============================================================================
# Internationalization
# ============================================================================

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ============================================================================
# Static Files + Project Root
# ============================================================================

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# We have the folder river2ridge that houses all central settings etc. We want the outer folder of this (gpy_site)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'apps/core/static/'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# ============================================================================
# Static Files + Project Root
# ============================================================================

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = '/media/'

# ============================================================================
# Django Rest Framework
# ============================================================================

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# ============================================================================
# Celery
# ============================================================================

import djcelery

djcelery.setup_loader()

BROKER_URL = os.environ.get("RABBITMQ_BIGWIG_URL", 'amqp://admin:admin@rabbitmq:5672/river2ridge')
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# ============================================================================
# Logging
# ============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'INFO',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'river2ridge': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'core': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'web': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }

}
