# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
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

ALLOWED_HOSTS = ["*"]
