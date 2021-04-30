from django.urls import path
from django.views.generic import TemplateView

from core.views import (
    NotificationAddView,
    NotificationDetailView,
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
        "notification/<int:pk>/",
        NotificationDetailView.as_view(),
        name="notification_detail_view",
    ),
    path(
        "notification/add/", NotificationAddView.as_view(), name="notification_add_view"
    ),
    path(
        "instructions/",
        TemplateView.as_view(
            template_name="core/instructions.html",
            extra_context={"page_title": "Instructions"},
        ),
        name="instructions_view",
    ),
]
