from crum import get_current_user


def auto_save_current_user(instance):
    user = get_current_user()
    if user and not user.pk:
        user = None
    if not instance.pk:
        instance.created_by = user
    instance.updated_by = user
