from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from core.models import Notification

from core.forms import NotificationForm

# Create your views here.


class NotificationAddView(SuccessMessageMixin, CreateView):
    template_name = "core/notification_add_form.html"
    form_class = NotificationForm
    extra_context = {"page_title": "Add Notification"}
    success_message = "Successfully added the Notification"


class NotificationsListView(ListView):
    template_name = "core/notifications_list.html"
    extra_context = {"page_title": "Notifications"}
    queryset = Notification.objects.all()
