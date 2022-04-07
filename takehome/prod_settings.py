from pathlib import Path

import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unniku$default',
        'USER': 'unniku',
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': 'unniku.mysql.pythonanywhere-services.com>',
    }
}


ALLOWED_HOSTS = ['unniku.pythonanywhere']
MEDIA_ROOT = BASE_DIR/'media/'