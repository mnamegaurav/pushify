from django.urls import path

from websites.views import WebsiteAddView, WebsiteEditView

app_name = "websites"

urlpatterns = [
    path("website/add/", WebsiteAddView.as_view(), name="website_add_view"),
    path("website/edit/<int:pk>/", WebsiteEditView.as_view(), name="website_edit_view"),
]
