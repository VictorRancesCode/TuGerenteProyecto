import os
from .base import *
import dj_database_url

DEBUG = False





ALLOWED_HOSTS = ['https://tu-gerente-booking.herokuapp.com']



DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.setdefault('DATABASE_URL', '')
    )
}