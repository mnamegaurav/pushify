from django.urls import path
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from accounts.views import (
    UserProfileView,
    CustomLoginView,
    RegisterView,
    CustomLogoutView,
)

app_name = "accounts"

urlpatterns = [
    path(
        "",
        CustomLoginView.as_view(),
        name="login_view",
    ),
    path(
        "profile/",
        UserProfileView.as_view(),
        name="user_profile_view",
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register_view",
    ),
    path(
        "logout/",
        CustomLogoutView.as_view(),
        name="logout_view",
    ),
    path(
        "password/forgot/",
        PasswordResetView.as_view(
            email_template_name="accounts/password_forgot.html",
            template_name="accounts/password_forgot.html",
            success_url=reverse_lazy("accounts:password_forgot_done_view"),
            extra_context={"page_title": "Forgot Password"},
        ),
        name="password_forgot_view",
    ),
    path(
        "password/forgot/done/",
        PasswordResetDoneView.as_view(
            template_name="accounts/password_forgot_done.html",
            extra_context={"page_title": "Forgot Password"},
        ),
        name="password_forgot_done_view",
    ),
    path(
        "password/forgot/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="accounts/password_forgot_confirm.html",
            success_url=reverse_lazy("accounts:password_forgot_complete_view"),
            extra_context={"page_title": "Forgot Password"},
        ),
        name="password_forgot_confirm_view",
    ),
    path(
        "password/forgot/complete/",
        PasswordResetCompleteView.as_view(
            template_name="accounts/password_forgot_complete.html",
            extra_context={"page_title": "Forgot Password"},
        ),
        name="password_forgot_complete_view",
    ),
    path(
        "password/change/",
        login_required(
            PasswordChangeView.as_view(
                template_name="accounts/password_change.html",
                success_url=reverse_lazy("accounts:password_change_done_view"),
                extra_context={"page_title": "Change Password"},
            )
        ),
        name="password_change_view",
    ),
    path(
        "password/change/done/",
        login_required(
            PasswordResetDoneView.as_view(
                template_name="accounts/password_change_done.html",
                extra_context={"page_title": "Change Password"},
            )
        ),
        name="password_change_done_view",
    ),
]
