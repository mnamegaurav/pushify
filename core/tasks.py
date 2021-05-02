from celery import shared_task

from core.models import Notification
from core.utils import send_notifications_in_bulk


@shared_task
def send_notifications_in_bulk_task(website_id, *args, **kwargs):

    response = send_notifications_in_bulk(website_id, *args, **kwargs)

    return
