import os
from .base import *
import dj_database_url

DEBUG = False
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ALLOWED_HOSTS = ['tu-gerente-booking.herokuapp.com','.herokuapp.com']
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.setdefault('DATABASE_URL', '')
    )
}