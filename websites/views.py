from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from websites.models import Website

from websites.forms import WebsiteForm

# Create your views here.


class WebsiteAddView(SuccessMessageMixin, CreateView):
    template_name = "websites/website_add_form.html"
    form_class = WebsiteForm
    extra_context = {"page_title": "Add Website"}
    success_message = "Successfully added the website"


class WebsiteEditView(SuccessMessageMixin, UpdateView):
    template_name = "websites/website_edit_form.html"
    form_class = WebsiteForm
    pk_url_kwarg = "pk"
    extra_context = {"page_title": "Website Details"}
    success_message = "Successfully saved the changes"
    queryset = Website.objects.filter(is_active=True)


class WebsitesListView(ListView):
    template_name = "websites/websites_list.html"
    extra_context = {"page_title": "My Websites"}
    queryset = Website.objects.filter(is_active=True)
