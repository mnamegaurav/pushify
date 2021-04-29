"""notification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from rest_framework.routers import DefaultRouter

from fcm_django.api.rest_framework import FCMDeviceViewSet, FCMDeviceAuthorizedViewSet


router = DefaultRouter()
router.register("devices", FCMDeviceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # /, /login, /register, /forgot-password
    path("", include("accounts.urls")),
    # dashboard/,
    path("", include("analytics.urls")),
    # website/add/, website/delete/<id>/, website/edit/<id>/, website/<id>
    path("", include("core.urls")),
    path("api/fcm/", include(router.urls)),
    re_path(
        r"^firebase-messaging-sw.js",
        TemplateView.as_view(
            template_name="firebase-messaging-sw.js",
            content_type="application/javascript",
        ),
    ),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


def error_page(request, *args, **kwargs):
    return render(request, "404.html")


handler404 = error_page
handler500 = error_page
handler403 = error_page
handler400 = error_page
