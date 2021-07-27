CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r"^/api/fcm/device/create/.*$"

CORS_ALLOW_METHODS = [
    "POST",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}
