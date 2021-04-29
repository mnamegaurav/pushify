from django.urls import path
from django.views.generic import TemplateView

from core.views import (
    NotificationAddView,
    NotificationsListView,
)

app_name = "core"

urlpatterns = [
    path(
        "dashboard/",
        TemplateView.as_view(template_name="core/home.html"),
        name="home_view",
    ),
    path(
        "notifications/",
        NotificationsListView.as_view(),
        name="notifications_list_view",
    ),
    path(
        "notification/add/", NotificationAddView.as_view(), name="notification_add_view"
    ),
    path(
        "instructions/",
        TemplateView.as_view(template_name="core/instructions.html"),
        name="instructions_view",
    ),
]
