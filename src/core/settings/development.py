from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@hx6glnj!7^ntl5qmq%@m!7)fkd6nnt9owzju25qrcov*u06l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

