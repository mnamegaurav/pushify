from django.contrib import admin

from websites.models import Website

# Register your models here.
@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    model = Website
    list_display = (
        "url",
        "title",
        "created_by",
        "updated_by",
        "created_on",
        "updated_on",
    )
