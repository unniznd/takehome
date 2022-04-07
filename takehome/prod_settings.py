from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "os.environ.get('SECRET_KEY')"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['localhost']
MEDIA_ROOT = BASE_DIR/'media/'