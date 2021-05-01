from django.contrib import admin

from fcm_django.admin import DeviceAdmin
from fcm_django.models import FCMDevice

from core.models import Notification, FCMTokenDevice

# Register your models here.

admin.site.unregister(FCMDevice)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ("title", "get_status", "website", "created_on")

    def get_status(self, obj):
        return obj.status

    get_status.short_description = "Notification Task Status"


@admin.register(FCMTokenDevice)
class FCMTokenDeviceAdmin(DeviceAdmin):
    model = FCMTokenDevice
    list_display = list(DeviceAdmin.list_display) + ["website"]
