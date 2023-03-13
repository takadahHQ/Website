from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "takadah-dev-%$)wg^oewabdu(@&ai^v793brks2q20ehlu(sjn#(x+3+^$*tq"

DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = ["*"]


INTERNAL_IPS = [
    "127.0.0.1",
]
INSTALLED_APPS += [
    "django_browser_reload",
    "debug_toolbar",
    #'django_fastdev',
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# #Local
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "takadah",
    #     "USER": "maximus",
    #     "PASSWORD": "Z!nox2018",
    #     "HOST": "database-1.czkumzmsnn55.ap-northeast-1.rds.amazonaws.com",
    #     "PORT": "5432",
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
]
