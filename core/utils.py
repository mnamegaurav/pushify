from core.models import FCMTokenDevice


def send_notifications_in_bulk(website_id, *args, **kwargs):

    # collect all the kwargs
    title = kwargs.get("title", "")
    body = kwargs.get("body", "")
    icon_url = kwargs.get("icon_url", "")
    banner_url = kwargs.get("banner_url", "")
    launch_url = kwargs.get("launch_url", "")

    # prepare data dict for fcm notifications(messages)
    data = {
        "image_url": banner_url,
        "launch_url": launch_url,
        "icon_url": icon_url,
    }

    # curate all the tokens of this website
    fcm_token_devices = FCMTokenDevice.objects.filter(website_id=website_id)

    # send finals notifications in bulk mode
    response = fcm_token_devices.send_message(
        title=title,
        body=body,
        icon=icon_url,
        data=data,
    )

    return response
