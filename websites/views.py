from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from websites.models import Website

from websites.forms import WebsiteForm

# Create your views here.


class WebsiteAddView(CreateView):
    template_name = "websites/website_add_form.html"
    form_class = WebsiteForm
    extra_context = {"page_title": "Add Website"}


class WebsiteEditView(UpdateView):
    template_name = "websites/website_edit_form.html"
    form_class = WebsiteForm
    pk_url_kwarg = "pk"
    extra_context = {"page_title": "Edit Website Details"}
    queryset = Website.objects.filter(is_active=True)
