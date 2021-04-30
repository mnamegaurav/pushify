from django.contrib import admin

from fcm_django.admin import DeviceAdmin
from fcm_django.models import FCMDevice

from core.models import Notification, FCMTokenDevice

# Register your models here.

admin.site.unregister(FCMDevice)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification


@admin.register(FCMTokenDevice)
class FCMTokenDeviceAdmin(DeviceAdmin):
    model = FCMTokenDevice
    list_display = list(DeviceAdmin.list_display) + ["website"]
