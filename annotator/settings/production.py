from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'cap_nvd',
        'USER': 'admin',
        'PASSWORD': 'Peroni4me',
        'HOST': 'db',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

