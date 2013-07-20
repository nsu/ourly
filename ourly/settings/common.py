import os

from django.conf.global_settings import *


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'timer'
)
LOGIN_URL = '/login/'
ROOT_URLCONF = 'ourly.urls'
SECRET_KEY = os.environ.get('SECRET_KEY', 'JHJSDFHSFY&(Y&*S*FG*SKHSF(*Y*(S(F')
SETTINGS_MODULE = 'ourly.settings.prod'
SITE_ID = 1
STATIC_URL = '/static/'
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'ourly.wsgi.application'


DEBUG = True
TEMPLATE_DEBUG = DEBUG

import dj_database_url
DATABASES['default'] = dj_database_url.config()
if not DATABASES['default']:
    from .common import *
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': './db.sqlite',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
