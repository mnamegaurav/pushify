from django import forms
from core.models import Notification


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"
        exclude = (
            "celery_task_id",
            "failure_count",
            "success_count",
            "created_by",
            "updated_by",
        )
