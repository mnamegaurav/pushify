from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.models import Notification
from core.forms import NotificationForm
from core.tasks import send_notifications_in_bulk_task

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"


class NotificationAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "core/notification_add_form.html"
    form_class = NotificationForm
    extra_context = {"page_title": "Add Notification"}
    success_message = "Notifications are in queue, we are just sending it."
    queryset = Notification.objects.all()

    def push_celery_task(self, form):
        # send this data to the notification task
        website_id = form.instance.website.pk
        title = form.instance.title
        body = form.instance.body

        if form.instance.launch_url:
            launch_url = form.instance.launch_url
        else:
            launch_url = None

        if form.instance.icon:
            icon_url = form.instance.icon.url
        else:
            icon_url = None

        if form.instance.banner:
            banner_url = form.instance.banner.url
        else:
            banner_url = None

        try:
            send_notifications_in_bulk_task.apply_async(
                args=(website_id,),
                kwargs={
                    "title": title,
                    "body": body,
                    "launch_url": launch_url,
                    "icon_url": icon_url,
                    "banner_url": banner_url,
                },
            )
            print("sent the notification booyah!")
            return True
        except Exception as e:
            print(f"Error Executing the send notification task: \n{e}")
            return False

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            self.push_celery_task(form)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class NotificationDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/notification_detail.html"
    extra_context = {"page_title": "Notification Detail"}
    queryset = Notification.objects.all()


class NotificationsListView(LoginRequiredMixin, ListView):
    template_name = "core/notifications_list.html"
    extra_context = {"page_title": "Notifications"}
    queryset = Notification.objects.all()
