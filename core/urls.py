from django.urls import path
from django.views.generic import TemplateView

app_name = "core"

urlpatterns = [
    path(
        "dashboard/",
        TemplateView.as_view(template_name="core/home.html"),
        name="home_view",
    ),
]
