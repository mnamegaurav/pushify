from django.urls import path
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

app_name = "accounts"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="accounts/register.html"),
        name="register_view",
    ),
    path(
        "login/",
        TemplateView.as_view(template_name="accounts/login.html"),
        name="login_view",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout_view",
    ),
    path(
        "password/forgot/",
        PasswordResetView.as_view(
            email_template_name="accounts/password_forgot.html",
            template_name="accounts/password_forgot.html",
        ),
        name="password_forgot_view",
    ),
    path(
        "password/forgot/done/",
        PasswordResetDoneView.as_view(
            template_name="accounts/password_forgot_done.html"
        ),
        name="password_forgot_done_view",
    ),
    path(
        "password/forgot/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="accounts/password_forgot_confirm.html"
        ),
        name="password_forgot_confirm_view",
    ),
    path(
        "password/forgot/complete/",
        PasswordResetCompleteView.as_view(
            template_name="accounts/password_forgot_complete.html"
        ),
        name="password_forgot_complete_view",
    ),
    path(
        "password/change/",
        PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url=reverse_lazy("password_change_done_view"),
        ),
        name="password_change_view",
    ),
    path(
        "password/change/done/",
        PasswordResetDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done_view",
    ),
]
