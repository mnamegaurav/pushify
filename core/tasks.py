from celery import shared_task, current_task

from core.models import Notification
from core.utils import send_notifications_in_bulk


@shared_task
def send_notifications_in_bulk_task(website_id, *args, **kwargs):

    response = send_notifications_in_bulk(website_id, *args, **kwargs)
    celery_task_id = current_task.request.id

    try:
        notification_obj = Notification.objects.get(celery_task_id=celery_task_id)
        notification_obj.success_count = response.get("success", 0)
        notification_obj.failure_count = response.get("failure", 0)
        notification_obj.save(update_fields=["success_count", "failure_count"])
    except Exception as e:
        raise e

    return
