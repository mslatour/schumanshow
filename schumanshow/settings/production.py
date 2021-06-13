import os
import django_heroku

from .base import *

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())
