from django.urls import path

from websites.views import (
    WebsiteAddView,
    WebsiteEditView,
    WebsitesListView,
    WebsiteDeleteView,
)

app_name = "websites"

urlpatterns = [
    path("websites/", WebsitesListView.as_view(), name="websites_list_view"),
    path("website/add/", WebsiteAddView.as_view(), name="website_add_view"),
    path(
        "website/edit/<slug:slug>/", WebsiteEditView.as_view(), name="website_edit_view"
    ),
    path(
        "website/delete/<int:pk>/",
        WebsiteDeleteView.as_view(),
        name="website_delete_view",
    ),
]
