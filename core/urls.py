from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from core.views import (
    HomeView,
    NotificationAddView,
    NotificationDetailView,
    NotificationsListView,
)

app_name = "core"

urlpatterns = [
    path(
        "dashboard/",
        HomeView.as_view(),
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
        login_required(
            TemplateView.as_view(
                template_name="core/instructions.html",
                extra_context={"page_title": "Instructions"},
            )
        ),
        name="instructions_view",
    ),
]
