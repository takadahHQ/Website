from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "Takadah-%$)wg^oeyeezyu(@&ai^v793brks2q20pweey(sjn#(x+3+^$*tq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ebdb",
        "USER": "takadah",
        "PASSWORD": "Z!nox2018",
        "HOST": "https://ap-northeast-1.console.aws.amazon.com/rds/home?region=ap-northeast-1#dbinstances:id=awseb-e-8dwr2i3ifw-stack-awsebrdsdatabase-xpxkebkzgtze",
        "PORT": "5432",
        # "CERT": "prod-ca-2021.crt",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

STATIC_URL = "static/"
# STATIC_ROOT = '/home/takalqei/takadah-app/static/'

MEDIA_URL = "/media/"
# MEDIA_ROOT = '/home/takalqei/takadah-app/media/'


# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = False

# SECURE_HSTS_SECONDS = 3153600 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAIN = True
