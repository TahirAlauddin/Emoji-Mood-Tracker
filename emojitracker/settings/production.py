from base import *
import os

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.netlify.app']

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


