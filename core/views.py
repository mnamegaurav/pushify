from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from django_celery_results.models import TaskResult

from core.models import Notification
from core.forms import NotificationForm
from core.tasks import send_notifications_in_bulk_task
from core.mixins import QuerySetMixin

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"


class NotificationAddView(
    LoginRequiredMixin, SuccessMessageMixin, QuerySetMixin, CreateView
):
    model = Notification
    template_name = "core/notification_add_form.html"
    form_class = NotificationForm
    extra_context = {"page_title": "Add Notification"}
    success_message = "Notifications are in queue, we are just sending it."

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
            task = send_notifications_in_bulk_task.apply_async(
                args=(website_id,),
                kwargs={
                    "title": title,
                    "body": body,
                    "launch_url": launch_url,
                    "icon_url": icon_url,
                    "banner_url": banner_url,
                },
            )
            print(f"sent the notification booyah! {task.state}")
            return task.id
        except Exception as e:
            print(f"Error Executing the send notification task: \n{e}")

        return None

    def get(self, request, *args, **kwargs):
        query_notification_id = request.GET.get("notification_id")
        if query_notification_id:
            try:
                notification_obj = Notification.objects.get(
                    pk=query_notification_id, created_by=request.user
                )
                notification_obj_dict = model_to_dict(notification_obj)
                self.initial = notification_obj_dict
            except ObjectDoesNotExist:
                pass
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():

            # send the task to celery
            task_id = self.push_celery_task(form)

            # save the task id into database
            form.instance.celery_task_id = task_id

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        queryset = Notification.objects.filter(created_by=self.request.user)
        return queryset


class NotificationDetailView(LoginRequiredMixin, QuerySetMixin, DetailView):
    model = Notification
    template_name = "core/notification_detail.html"
    extra_context = {"page_title": "Notification Detail"}

    def get_queryset(self):
        queryset = Notification.objects.filter(created_by=self.request.user)
        return queryset


class NotificationsListView(LoginRequiredMixin, QuerySetMixin, ListView):
    model = Notification
    template_name = "core/notifications_list.html"
    extra_context = {"page_title": "Notifications"}

    def get_queryset(self):
        queryset = Notification.objects.filter(created_by=self.request.user)
        return queryset
