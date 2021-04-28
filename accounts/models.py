from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    picture = models.ImageField(upload_to="", null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "full_name",
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
