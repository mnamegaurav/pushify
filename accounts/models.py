from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.conf import settings

from accounts.managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=50,
        verbose_name=_("Username"),
        unique=True,
        validators=(MinLengthValidator(settings.MIN_USERNAME_LENGTH),),
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "full_name",
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
