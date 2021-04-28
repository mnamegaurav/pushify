FCM_DJANGO_SETTINGS = {
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "FCM Django Notifications",
    # Your firebase API KEY
    "FCM_SERVER_KEY": "AAAAfQeIje0:APA91bFhhOu_E-nU4QeC7OoPRKG3FjDxHZTbi1l0RTcaEpjWqUopS1EgqLYYvUg5fbXgp-CYeObIcHO3_jJyIU2TvzyWZSxDYaShhXUYefjjVSexxnSGObBDd28BzVbjhHVlAwcjIuB3",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}
