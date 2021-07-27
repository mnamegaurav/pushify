from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts.models import User


User = get_user_model()

# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_editable = ("is_active",)
    list_display = (
        "email",
        "full_name",
        "username",
        "is_active",
    )
    add_fieldsets = (
        (
            "Personal Details",
            {
                "fields": (
                    "email",
                    "full_name",
                    "username",
                    "picture",
                    "password1",
                    "password2",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    fieldsets = (
        ("Personal Details", {"fields": ("email", "full_name", "username", "picture")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
