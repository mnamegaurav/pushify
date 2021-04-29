from django.urls import path

from websites.views import (
    WebsiteAddView,
    WebsiteEditView,
    WebsitesListView,
)

app_name = "websites"

urlpatterns = [
    path("websites/", WebsitesListView.as_view(), name="websites_list_view"),
    path("website/add/", WebsiteAddView.as_view(), name="website_add_view"),
    path("website/edit/<int:pk>/", WebsiteEditView.as_view(), name="website_edit_view"),
]
