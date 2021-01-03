from .base import *
import os

DEBUG = False

INSTALLED_APPS += ['storages']

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.studycollaboration.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_DATABASE'),
        'USER': os.environ.get('DB_USERNAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'TIMEOUT': None
    },
}

CACHE_MIDDLEWARE_SECONDS = 7 * 24 * 60 * 60

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'base.storages.S3StaticStorage'
AWS_STORAGE_BUCKET_NAME = 'wou-media-production'
AWS_STATIC_BUCKET_NAME = 'wou-static-production'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False


SITE_URL = 'https://studycollaboration.com'

AWS_S3_CUSTOM_DOMAIN = 'media.studycollaboration.com'
AWS_STATIC_CUSTOM_DOMAIN = 'static.studycollaboration.com'
STATIC_URL = 'https://static.studycollaboration.com/'
MEDIA_URL = 'https://media.studycollaboration.com/'