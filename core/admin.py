from django.contrib import admin

from fcm_django.admin import DeviceAdmin
from fcm_django.models import FCMDevice

from core.models import Notification, FCMDeviceToken

# Register your models here.

admin.site.unregister(FCMDevice)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification


@admin.register(FCMDeviceToken)
class FCMDeviceTokenAdmin(DeviceAdmin):
    model = FCMDeviceToken
    list_display = list(DeviceAdmin.list_display) + ["website"]
