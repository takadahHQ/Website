import os
from pathlib import Path
import diskcache
from .backends import StaticStorage, PublicMediaStorage
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# sys.path.append(os.path.join(settings.BASE_DIR, "modules"))

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "Takadah-%$)wg^oewabdu(@&ai^v793brks30Retehlu(sjn#(x+3+^$*tq"

AUTH_USER_MODEL = "core.Users"
STORIES_MODEL = "stories.Stories"
# LOGIN_REDIRECT_URL = "core:index"
LOGIN_URL = "two_factor:login"

# this one is optional
LOGIN_REDIRECT_URL = "two_factor:profile"
LOGOUT_REDIRECT_URL = "core:index"

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

NPM_BIN_PATH = r"C:\laragon\bin\nodejs\node-v18\npm.cmd"
SITE_ID = 1

STRIPE_LIVE_SECRET_KEY = "sk_live_fddfkflkdfkdfldfk"
STRIPE_TEST_SECRET_KEY = "sk_test_l;dkjpwojrwpowrogwrpwprf"
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
DJSTRIPE_USE_NATIVE_JSONFIELD = (
    True  # We recommend setting to True for new installations
)
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    "www.takadah.com",
    "takadah.com",
    "127.0.0.1",
    "*",
]

HIJACK_ALLOW_GET_REQUESTS = True
HIJACK_PERMISSION_CHECK = "hijack.permissions.superusers_and_staff"

X_FRAME_OPTIONS = "SAMEORIGIN"
# SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Application definition

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "flags",
    "tailwind",
    "analytical",
    # "cookie_consent",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_email",
    "two_factor",
    "two_factor.plugins.email",
    "crispy_forms",
    "crispy_tailwind",
    "extra_views",
    "braces",
    "fontawesomefree",
    #'auditlog',
    "ckeditor",
    "ckeditor_uploader",
    "hijack",
    "hijack.contrib.admin",
    "import_export",
    "flag",
    "watson",
    "ipware",
    "reversion",
    "newsfeed",
    "taggit",
    # "djstripe",
    "storages",
]

LOCAL_APPS = [
    # "theme",
    "modules.core",
    "modules.pages",
    "modules.blog",
    "modules.stories",
    "modules.adverts",
    "modules.subscriptions",
    # "modules.helpdesk",
    # "modules.roadmap",
    # "modules.stats",
    "modules.theme",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "watson.middleware.SearchContextMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "hijack.middleware.HijackUserMiddleware",
    # "djstripe.middleware.SubscriptionPaymentMiddleware",
    # "modules.stats.middleware.AnalyticsMiddleware",
    # 'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = "takadah.urls"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
# s3 static settings
AWS_STATIC_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"
STATICFILES_STORAGE = "StaticStorage"
# s3 public media settings
AWS_MEDIA_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "PublicMediaStorage"

CACHES = {
    "default": {
        "BACKEND": "diskcache.DjangoCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),
        "TIMEOUT": 300,
        # ^-- Django setting for default timeout of each key.
        "SHARDS": 8,
        "DATABASE_TIMEOUT": 0.010,  # 10 milliseconds
        # ^-- Timeout for each DjangoCache database transaction.
        "OPTIONS": {"size_limit": 2**30},  # 1 gigabyte
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "resources")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                # "modules.core.context_processor.settings",
                # "modules.core.context_processor.socials",
                # "modules.core.context_processor.menus",
            ],
        },
    },
]

WSGI_APPLICATION = "takadah.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

TAILWIND_APP_NAME = "modules.theme"
TAGGIT_CASE_INSENSITIVE = True

# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "resources/static"),
    BASE_DIR / "resources/static",
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_UPLOAD_PATH = "media/uploads"

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Takadah Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Takadah",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Takadah",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/logo-colored.svg",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Takadah",
    # Copyright on the footer
    "copyright": "Takadah",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "core.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "core:index"},
        # external url that opens in a new window (Permissions can be added)
        # {"name": "Admin Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "core.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "stories"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["auth"],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "core.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}

CKEDITOR_CONFIGS = {
    "default": {
        #'skin': 'moono',
        #'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Save",
                    "NewPage",
                    "Preview",
                    "Print",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #            'HiddenField']},
            # '/',
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            # {'name': 'insert',
            #  'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
            # {'name': 'about', 'items': ['About']},
            "/",  # put this to force next toolbar on new line
            # {'name': 'yourcustomtools', 'items': [
            #     # put the name of your editor.ui.addButton here
            #     'Preview',
            #     'Maximize',
            # ]},
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        "toolbarGroups": [
            {"name": "document", "groups": ["mode", "document", "doctools"]}
        ],
        # 'height': 291,
        "width": "100%",
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 2,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}

MIXPANEL_API_TOKEN = os.environ.get("MIXPANEL_API_TOKEN")
MATOMO_DOMAIN_PATH = "mamoto.takadah.com"
MATOMO_SITE_ID = "1"
# ANALYTICAL_INTERNAL_IPS = ['192.168.1.45', '192.168.1.57']
ANALYTICAL_AUTO_IDENTIFY = True


# GeoIP

MAXMIND_CITY_DB = os.getenv("MAXMIND_CITY_DB", "resources/geoip/GeoLite2-City.mmdb")
MAXMIND_ASN_DB = os.getenv("MAXMIND_ASN_DB", "resources/geoip/GeoLite2-ASN.mmdb")


# Email

SERVER_EMAIL = os.getenv("SERVER_EMAIL", "Takadah <noreply@takadah.com>")
DEFAULT_FROM_EMAIL = SERVER_EMAIL
if DEBUG or os.environ.get("EMAIL_HOST") is None:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST", "takadah.com")
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")
    EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)

# Auto fields
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# NPM

NPM_ROOT_PATH = "../"

NPM_FILE_PATTERNS = {
    "a17t": [os.path.join("dist", "a17t.css"), os.path.join("dist", "tailwind.css")],
    "apexcharts": [os.path.join("dist", "apexcharts.min.js")],
    "litepicker": [
        os.path.join("dist", "nocss", "litepicker.js"),
        os.path.join("dist", "css", "litepicker.css"),
        os.path.join("dist", "plugins", "ranges.js"),
    ],
    "turbolinks": [os.path.join("dist", "turbolinks.js")],
    "stimulus": [os.path.join("dist", "stimulus.umd.js")],
    "inter-ui": [os.path.join("Inter (web)", "*")],
    "@fortawesome": [os.path.join("fontawesome-free", "js", "all.min.js")],
    "datamaps": [os.path.join("dist", "datamaps.world.min.js")],
    "d3": ["d3.min.js"],
    "topojson": [os.path.join("build", "topojson.min.js")],
    "flag-icon-css": [
        os.path.join("css", "flag-icon.min.css"),
        os.path.join("flags", "*"),
    ],
}

# Shynet

# Can everyone create services, or only superusers?
# Note that in the current version of Shynet, being able to edit a service allows
# you to see every registered user on the Shynet instance. This will be changed in
# a future version.
ONLY_SUPERUSERS_CREATE = os.getenv("ONLY_SUPERUSERS_CREATE", "True") == "True"

# Should the script use HTTPS to send the POST requests? The hostname is from
# the django SITE default. (Edit it using the admin panel.)
SCRIPT_USE_HTTPS = os.getenv("SCRIPT_USE_HTTPS", "True") == "True"

# How frequently should the tracking script "phone home" with a heartbeat, in
# milliseconds?
SCRIPT_HEARTBEAT_FREQUENCY = int(os.getenv("SCRIPT_HEARTBEAT_FREQUENCY", "5000"))

# How much time can elapse between requests from the same user before a new
# session is created, in seconds?
SESSION_MEMORY_TIMEOUT = int(os.getenv("SESSION_MEMORY_TIMEOUT", "1800"))

# Should the Shynet version information be displayed?
SHOW_SHYNET_VERSION = os.getenv("SHOW_SHYNET_VERSION", "True") == "True"

# Should Shynet show third-party icons in the dashboard?
SHOW_THIRD_PARTY_ICONS = os.getenv("SHOW_THIRD_PARTY_ICONS", "True") == "True"

# Should Shynet never collect any IP?
BLOCK_ALL_IPS = os.getenv("BLOCK_ALL_IPS", "False") == "True"

# Include date and service ID in salt?
AGGRESSIVE_HASH_SALTING = os.getenv("AGGRESSIVE_HASH_SALTING", "False") == "True"

# What location url should be linked to in the frontend?
LOCATION_URL = os.getenv(
    "LOCATION_URL", "https://www.openstreetmap.org/?mlat=$LATITUDE&mlon=$LONGITUDE"
)

# How many services should be displayed on dashboard page?
DASHBOARD_PAGE_SIZE = int(os.getenv("DASHBOARD_PAGE_SIZE", "5"))

# Should background bars be scaled to full width?
USE_RELATIVE_MAX_IN_BAR_VISUALIZATION = (
    os.getenv("USE_RELATIVE_MAX_IN_BAR_VISUALIZATION", "True") == "True"
)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["GET", "OPTIONS"]

# IPWare Precedence Options
IPWARE_META_PRECEDENCE_ORDER = (
    "HTTP_CF_CONNECTING_IP",
    "HTTP_X_FORWARDED_FOR",
    "X_FORWARDED_FOR",  # client, proxy1, proxy2
    "HTTP_CLIENT_IP",
    "HTTP_X_REAL_IP",
    "HTTP_X_FORWARDED",
    "HTTP_X_CLUSTER_CLIENT_IP",
    "HTTP_FORWARDED_FOR",
    "HTTP_FORWARDED",
    "HTTP_VIA",
    "REMOTE_ADDR",
)
