from django.urls import path
from django.views.generic import TemplateView

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
        "forgot-password/",
        TemplateView.as_view(template_name="accounts/forgot_password.html"),
        name="forgot_password_view",
    ),
    path(
        "change-password/",
        TemplateView.as_view(template_name="accounts/change_password.html"),
        name="change_password_view",
    ),
]
