from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Takadah-%$)wg^oeyeezyu(@&ai^v793brks2q20pweey(sjn#(x+3+^$*tq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['takadah.com', '127.0.0.1']

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'takalqei_django',
#         'USER': 'takalqei_django',
#         'PASSWORD': 'Z!nox2018',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

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

STATIC_URL = '/assets/'
STATIC_ROOT = '/home/takalqei/takadah-app/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/takalqei/takadah-app/media/'

#CLICKMAP_TRACKER_ID = 'XXXXXXXX'
#CRAZY_EGG_ACCOUNT_NUMBER = '12345678'
MIXPANEL_API_TOKEN = 'dc4537f245806621832017184b5f7d0c'
MATOMO_DOMAIN_PATH = 'mamoto.takadah.com'
MATOMO_SITE_ID = '1'
ANALYTICAL_INTERNAL_IPS = ['192.168.1.45', '192.168.1.57']
ANALYTICAL_AUTO_IDENTIFY = True