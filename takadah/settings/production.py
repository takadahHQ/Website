from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Takadah-%$)wg^oeyeezyu(@&ai^v793brks2q20pweey(sjn#(x+3+^$*tq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'takalqei_django',
        'USER': 'takalqei_django',
        'PASSWORD': 'Z!nox2018',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATIC_URL = 'static/'
# STATIC_ROOT = '/home/takalqei/takadah-app/static/'

MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home/takalqei/takadah-app/media/'


# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = False

# SECURE_HSTS_SECONDS = 3153600 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAIN = True