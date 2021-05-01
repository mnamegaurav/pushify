from django import forms
from core.models import Notification


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"
        exclude = ("task_result",)
