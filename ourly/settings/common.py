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
SETTINGS_MODULE = 'ourly.settings.dev'
SITE_ID = 1
STATIC_URL = '/static/'
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'ourly.wsgi.application'


DEBUG = True
TEMPLATE_DEBUG = DEBUG
