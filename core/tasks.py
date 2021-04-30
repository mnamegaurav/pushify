from celery import shared_task

from core.models import Notification


@shared_task
def send_notifications_in_bulk(fcm_token_devices, *args, **kwargs):

    # collect all the kwargs
    notification_title = kwargs.get("title", "")
    notification_body = kwargs.get("body", "")
    notification_icon_url = kwargs.get("icon_url", "")
    notification_banner_url = kwargs.get("notification_banner_url", "")
    notification_extra_data = kwargs.get("notification_extra_data", None)

    # prepare data dict for fcm notifications(messages)
    notification_data = {
        "image": notification_banner_url,
    }

    # add extra data into data dict
    if notification_extra_data:
        notification_data.update(notification_extra_data)

    # send finals notifications in bulk mode
    fcm_token_devices.send_message(
        title=notification_title,
        body=notification_body,
        icon=notification_icon_url,
        data=notification_data,
    )

    return
