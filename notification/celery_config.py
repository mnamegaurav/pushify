# Celery Configuration Options
CELERY_TIMEZONE = "Asia/Calcutta"
CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_BROKER_URL = "amqp://gaurav:gaurav@localhost:5672//localhost"
CELERY_CACHE_BACKEND = "default"


# Django Celery Results Configs
CELERY_RESULT_BACKEND = "django-db"
