from django.urls import path
from django.views.generic import TemplateView

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/home.html"), name="home_view"),
    path("login/", TemplateView.as_view(template_name="accounts/login.html")),
    path("register/", TemplateView.as_view(template_name="accounts/register.html")),
    path(
        "forgot-password/",
        TemplateView.as_view(template_name="accounts/forgot-password.html"),
    ),
]
