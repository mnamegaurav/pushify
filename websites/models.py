from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from crum import get_current_user

User = get_user_model()

# Create your models here.
class Website(models.Model):
    domain = models.CharField(
        max_length=255,
        verbose_name=_("Website Doamin"),
        unique=True,
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Website Name"),
    )
    created_by = models.ForeignKey(
        User,
        related_name="website_cb",
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
        default=None,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="website_ub",
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
        default=None,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"
        ordering = ("-created_on",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)
