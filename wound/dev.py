
from .base import *


DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


SITE_URL = 'http://127.0.0.1:8000/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_URL = '/uploads/'

SITE_URL = 'http://127.0.0.1:8000'
