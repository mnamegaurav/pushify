from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin

from core.models import Notification, FCMTokenDevice
from core.forms import NotificationForm
from core.tasks import send_notifications_in_bulk

# Create your views here.


class NotificationAddView(SuccessMessageMixin, CreateView):
    template_name = "core/notification_add_form.html"
    form_class = NotificationForm
    extra_context = {"page_title": "Add Notification"}
    success_message = "Notifications are in queue, we are just sending it."
    queryset = Notification.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():

            # get the current website to which notification is being sent
            website = form.instance.website

            # curate all the tokens of this website
            fcm_token_devices = FCMTokenDevice.objects.filter(website=website)

            # send all the notifications to all the fcm token
            # send_notifications_in_bulk(
            #     fcm_token_devices,
            # ).delay()
            print("sent the notification booyah!")

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class NotificationDetailView(DetailView):
    template_name = "core/notification_detail.html"
    extra_context = {"page_title": "Notification Detail"}
    queryset = Notification.objects.all()


class NotificationsListView(ListView):
    template_name = "core/notifications_list.html"
    extra_context = {"page_title": "Notifications"}
    queryset = Notification.objects.all()
