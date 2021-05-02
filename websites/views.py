from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from websites.models import Website
from websites.forms import WebsiteForm
from websites.mixins import PermissionQuerySetMixin

# Create your views here.


class WebsiteAddView(
    LoginRequiredMixin, SuccessMessageMixin, PermissionQuerySetMixin, CreateView
):
    model = Website
    template_name = "websites/website_add_form.html"
    form_class = WebsiteForm
    extra_context = {"page_title": "Add Website"}
    success_message = "Successfully added the website"

    def get_queryset(self):
        return self.get_website_queryset()


class WebsiteEditView(
    LoginRequiredMixin, SuccessMessageMixin, PermissionQuerySetMixin, UpdateView
):
    model = Website
    template_name = "websites/website_edit_form.html"
    form_class = WebsiteForm
    slug_field = "slug"
    slug_url_kwarg = "slug"
    extra_context = {"page_title": "Website Details"}
    success_message = "Successfully saved the changes"

    def get_queryset(self):
        return self.get_website_queryset()


class WebsiteDeleteView(
    LoginRequiredMixin, SuccessMessageMixin, PermissionQuerySetMixin, DeleteView
):
    model = Website
    success_message = "Successfully deleted the website"
    success_url = reverse_lazy("websites:websites_list_view")

    def get_queryset(self):
        return self.get_website_queryset()


class WebsitesListView(LoginRequiredMixin, PermissionQuerySetMixin, ListView):
    model = Website
    template_name = "websites/websites_list.html"
    extra_context = {"page_title": "My Websites"}

    def get_queryset(self):
        return self.get_website_queryset()
