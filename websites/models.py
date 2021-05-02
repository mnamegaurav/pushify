from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.urls import reverse_lazy

from accounts.utils import auto_save_current_user

User = get_user_model()

# Create your models here.
class Website(models.Model):
    url = models.URLField(
        verbose_name=_("Website URL"),
        help_text=_("Website URL i.e. - https://example.com/"),
        unique=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Website title"),
        help_text=_("Give a title to this website."),
    )
    slug = models.SlugField(editable=False, unique=True)
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
        return self.url

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        try:
            self.slug = slugify(self.title)
        except Exception as e:
            self.slug = f"{slugify(self.title)}-{self.pk}"
        # not using this line anymore
        # self.domain = urlparse(self.domain).netloc
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("websites:website_edit_view", args=[str(self.slug)])

    @property
    def subscribers_count(self):
        count = self.fcmtokendevice_website.count()
        return count
