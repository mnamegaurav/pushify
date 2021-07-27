from django import forms
from websites.models import Website


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = "__all__"
        exclude = ("is_active", "created_by", "updated_by", "slug")
