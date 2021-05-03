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
from core.mixins import PermissionQuerySetMixin

from websites.models import Website

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"


class NotificationAddView(
    LoginRequiredMixin, SuccessMessageMixin, PermissionQuerySetMixin, CreateView
):
    model = Notification
    template_name = "core/notification_add_form.html"
    form_class = NotificationForm
    extra_context = {"page_title": "Add Notification"}
    success_message = "Notifications are in queue, we are just sending it."

    def push_celery_task(self, instance):
        # send this data to the notification task
        website_id = instance.website.pk
        title = instance.title
        body = instance.body
        icon_url = (
            self.request.build_absolute_uri(instance.icon.url) if instance.icon else ""
        )
        banner_url = (
            self.request.build_absolute_uri(instance.banner.url)
            if instance.banner
            else ""
        )
        launch_url = instance.launch_url if instance.launch_url else ""

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
            return task.id
        except Exception as e:
            print(f"Error Executing the send notification task: \n{e}")

        return None

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["website"].queryset = Website.objects.filter(
            is_active=True, created_by=self.request.user
        )
        return form

    def get_initial(self):
        initial = super().get_initial()
        query_notification_id = self.request.GET.get("notification_id")
        if query_notification_id:
            try:
                notification_obj = Notification.objects.get(
                    pk=query_notification_id, created_by=self.request.user
                )
                notification_obj_dict = model_to_dict(notification_obj)
                initial.update(notification_obj_dict)
            except ObjectDoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        # send the task to celery
        task_id = self.push_celery_task(form.instance)

        # save the task id into database
        form.instance.celery_task_id = task_id

        # again save the instance
        form.instance.save(update_fields=["celery_task_id"])

        return response

    def get_queryset(self):
        return self.get_notification_queryset()


class NotificationDetailView(LoginRequiredMixin, PermissionQuerySetMixin, DetailView):
    model = Notification
    template_name = "core/notification_detail.html"
    extra_context = {"page_title": "Notification Detail"}

    def get_queryset(self):
        return self.get_notification_queryset()


class NotificationsListView(LoginRequiredMixin, PermissionQuerySetMixin, ListView):
    model = Notification
    template_name = "core/notifications_list.html"
    extra_context = {"page_title": "Notifications"}

    def get_queryset(self):
        return self.get_notification_queryset()
