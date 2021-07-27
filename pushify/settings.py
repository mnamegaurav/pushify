"""
Django settings for pushify project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import dotenv
from pathlib import Path

# Other Settings and Configs
from pushify.jazzmin_config import *
from pushify.drf_config import *
from pushify.celery_config import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# Application definition

INSTALLED_APPS = [
    # Jazzmin Admin theme
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.sites",

    # Third party apps
    "rest_framework",
    "corsheaders",
    "fcm_django",
    "crispy_forms",
    "django_celery_results",

    # Local apps
    "accounts.apps.AccountsConfig",
    "core.apps.CoreConfig",
    "analytics.apps.AnalyticsConfig",
    "websites.apps.WebsitesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "crum.CurrentRequestUserMiddleware",
]

ROOT_URLCONF = "pushify.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pushify.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-in"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = (BASE_DIR / "static_files",)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "accounts:login_view"
LOGIN_REDIRECT_URL = "core:home_view"
LOGOUT_REDIRECT_URL = LOGIN_URL
PASSWORD_RESET_TIMEOUT = 86400
# Custom property
MIN_USERNAME_LENGTH = 5

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache_table",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "emails"  # change this to a proper location

SITE_ID = 1

# CORS HEADERS SETTINGS
CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000']

CRISPY_TEMPLATE_PACK = "bootstrap4"

# fcm django settings
FCM_DJANGO_SETTINGS = {
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "FCM Django Notifications",
    # Your firebase API KEY
    "FCM_SERVER_KEY": os.environ["FCM_SERVER_KEY"],
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

"""
If you are running locally-
    1. Create a 'local_settings.py' in the same location of 'settings.py'
    2. Write 'DEBUG=True' in the 'local_settings.py' file.
"""
try:
    from pushify.local_settings import *
except ImportError:
    from pushify.prod_settings import *

if DEBUG:
    # All the settings when project is running locally

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    ALLOWED_HOSTS = ["*"]

    MIDDLEWARE.extend([
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ])

    INSTALLED_APPS.extend(
        [
            "django_extensions",
            "debug_toolbar",
        ]
    )

    INTERNAL_IPS = [
        "127.0.0.1",
    ]
else:
    ALLOWED_HOSTS = ["mnamegaurav-pushify.herokuapp.com", "*"]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PORT": os.environ["DB_PORT"],
            "HOST": os.environ["DB_HOST"],
            "PASSWORD": os.environ["DB_PASSWORD"],
        }
    }