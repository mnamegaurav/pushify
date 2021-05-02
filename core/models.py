from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from fcm_django.models import AbstractFCMDevice

from celery.result import AsyncResult

from django_celery_results.models import TaskResult

from accounts.utils import auto_save_current_user

from websites.models import Website

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    website = models.ForeignKey(
        Website, verbose_name=_("Website"), on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, verbose_name=_("Notification Title"))
    body = models.TextField(verbose_name=_("Notification Body"))
    icon = models.ImageField(upload_to="notification_icons", null=True, blank=True)
    banner = models.ImageField(upload_to="notification_banner", null=True, blank=True)
    launch_url = models.URLField(max_length=500, null=True, blank=True)
    success_count = models.PositiveBigIntegerField(
        verbose_name=_("Successfully Sent Count"), default=0, editable=False
    )
    failure_count = models.PositiveBigIntegerField(
        verbose_name=_("Failed to Sent Count"), default=0, editable=False
    )
    celery_task_id = models.TextField(null=True, blank=True, editable=False)
    created_by = models.ForeignKey(
        User,
        related_name="notification_cb",
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
        default=None,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="notification_ub",
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
        default=None,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notification History"
        verbose_name_plural = "Notification Histories"
        ordering = ("-created_on",)

    def __str__(self):
        return f"{self.website} - {self.title}"

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("core:notification_detail_view", args=[str(self.pk)])

    @property
    def status(self):
        try:
            res = AsyncResult(self.celery_task_id)
            status = res.state
        except Exception as e:
            status = "UNKNOWN"
        return status


class FCMTokenDevice(AbstractFCMDevice):
    website = models.ForeignKey(
        Website,
        verbose_name=_("Website"),
        on_delete=models.CASCADE,
        related_name="fcmtokendevice_website",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("FCM Token Device")
        verbose_name_plural = _("FCM Token Devices")
