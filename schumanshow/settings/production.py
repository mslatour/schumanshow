import os
import django_heroku

from .base import *

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
