from django.contrib import admin

from core.models import Notification

# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
