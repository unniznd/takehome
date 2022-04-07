from pathlib import Path
import os
import json
import cloudinary
import cloudinary_storage

BASE_DIR = Path(__file__).resolve().parent.parent


with open('secret_key.json') as f:
    secret = json.load(f)


SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['takehomeimager.herokuapp.com']

DATABASES = {
    "default": {
        "ENGINE": secret['ENGINE'],
        "NAME": secret['NAME'],
        "USER": secret['USER'],
        "PASSWORD":os.environ.get('PASSWORD'),
        "HOST":secret['HOST'],
        "PORT": secret['PORT']
    }
}
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': "dhw9oa5fm",
    'API_KEY': os.environ.get("API_KEY"),
    'API_SECRET': os.environ.get("API_SECRET"),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


