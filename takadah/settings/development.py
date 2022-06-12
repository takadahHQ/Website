from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'takadah-dev-%$)wg^oewabdu(@&ai^v793brks2q20ehlu(sjn#(x+3+^$*tq'

DEBUG = True

ALLOWED_HOSTS = ['takadah.com', '127.0.0.1']


INTERNAL_IPS = [
    '127.0.0.1',
]
INSTALLED_APPS += [
    'django_browser_reload',
    'debug_toolbar',
    #'django_fastdev',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
     ]

# #Local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    ]

#Local 
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "resources/static"),
   ]  
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#CLICKMAP_TRACKER_ID = 'XXXXXXXX'
#CRAZY_EGG_ACCOUNT_NUMBER = '12345678'
MIXPANEL_API_TOKEN = 'dc4537f245806621832017184b5f7d0c'
MATOMO_DOMAIN_PATH = 'matomo.takadah.com'
MATOMO_SITE_ID = '1'
ANALYTICAL_INTERNAL_IPS = ['192.168.1.45', '192.168.1.57']
ANALYTICAL_AUTO_IDENTIFY = True