from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("full_name", "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            "full_name",
            "picture",
            "email",
            "username",
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "full_name",
            "picture",
            "email",
            "username",
        )
