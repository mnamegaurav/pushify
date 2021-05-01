from core.models import FCMTokenDevice


def send_notifications_in_bulk(website_id, *args, **kwargs):

    # collect all the kwargs
    notification_title = kwargs.get("title", "")
    notification_body = kwargs.get("body", "")
    notification_icon_url = kwargs.get("icon_url", "")
    notification_banner_url = kwargs.get("banner_url", "")
    notification_launch_url = kwargs.get("launch_url", "")

    # prepare data dict for fcm notifications(messages)
    notification_data = {
        "image": notification_banner_url,
        "launch_url": notification_launch_url,
    }

    # curate all the tokens of this website
    fcm_token_devices = FCMTokenDevice.objects.filter(website_id=website_id)

    # send finals notifications in bulk mode
    response = fcm_token_devices.send_message(
        title=notification_title,
        body=notification_body,
        icon=notification_icon_url,
        data=notification_data,
    )

    return response
