from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

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
    slug_field = "slug"
    slug_url_kwarg = "slug"
    extra_context = {"page_title": "Website Details"}
    success_message = "Successfully saved the changes"
    queryset = Website.objects.filter(is_active=True)


class WebsiteDeleteView(SuccessMessageMixin, DeleteView):
    model = Website
    success_message = "Successfully deleted the website"
    success_url = reverse_lazy("websites:websites_list_view")


class WebsitesListView(ListView):
    template_name = "websites/websites_list.html"
    extra_context = {"page_title": "My Websites"}
    queryset = Website.objects.filter(is_active=True)
