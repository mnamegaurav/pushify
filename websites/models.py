from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.urls import reverse_lazy

from accounts.utils import auto_save_current_user

User = get_user_model()

# Create your models here.
class Website(models.Model):
    domain = models.CharField(
        max_length=255,
        verbose_name=_("Website Domain"),
        unique=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Website title"),
    )
    is_active = models.BooleanField(default=True)
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
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("websites:website_edit_view", args=[str(self.pk)])
