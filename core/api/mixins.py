from django.db.models import Q

from rest_framework import permissions
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    Serializer,
)

from fcm_django.settings import FCM_DJANGO_SETTINGS as SETTINGS

from urllib.parse import urlparse

from core.models import FCMTokenDevice
from core.api.permissions import IsOwner

from websites.models import Website


# Mixins
class DeviceSerializerMixin(ModelSerializer):
    class Meta:
        # fields = (
        #     "id",
        #     "name",
        #     "registration_id",
        #     "device_id",
        #     "website",
        #     "active",
        #     "date_created",
        #     "type",
        # )
        read_only_fields = ("date_created",)
        exclude = ("user", "website")
        extra_kwargs = {"active": {"default": True}}


class UniqueRegistrationSerializerMixin(Serializer):
    def validate(self, attrs):
        devices = None
        primary_key = None
        request_method = None

        if self.initial_data.get("registration_id", None):
            if self.instance:
                request_method = "update"
                primary_key = self.instance.id
            else:
                request_method = "create"
        else:
            if self.context["request"].method in ["PUT", "PATCH"]:
                request_method = "update"
                primary_key = self.instance.id
            elif self.context["request"].method == "POST":
                request_method = "create"

        Device = self.Meta.model
        # if request authenticated, unique together with registration_id and
        # user
        user = self.context["request"].user
        if request_method == "update":
            if user is not None and user.is_authenticated:
                devices = Device.objects.filter(
                    registration_id=attrs["registration_id"]
                ).exclude(id=primary_key)
                if attrs.get("active", False):
                    devices.filter(~Q(user=user)).update(active=False)
                devices = devices.filter(user=user)
            else:
                devices = Device.objects.filter(
                    registration_id=attrs["registration_id"]
                ).exclude(id=primary_key)
        elif request_method == "create":
            if user is not None and user.is_authenticated:
                devices = Device.objects.filter(
                    registration_id=attrs["registration_id"]
                )
                devices.filter(~Q(user=user)).update(active=False)
                devices = devices.filter(user=user, active=True)
            else:
                devices = Device.objects.filter(
                    registration_id=attrs["registration_id"]
                )

        if devices:
            raise ValidationError({"registration_id": "This field must be unique."})
        return attrs


class DeviceViewSetMixin(object):
    lookup_field = "registration_id"

    def perform_create(self, serializer):

        if self.request.user.is_authenticated:
            if SETTINGS["ONE_DEVICE_PER_USER"] and self.request.data.get(
                "active", True
            ):
                FCMTokenDevice.objects.filter(user=self.request.user).update(
                    active=False
                )
            return serializer.save(user=self.request.user)

        client_origin = self.request._request.META.get("HTTP_ORIGIN")

        if client_origin:
            # client_domain = urlparse(client_origin).netloc
            client_website = Website.objects.filter(url__contains=client_origin)

            if client_website.count() == 1:
                return serializer.save(website=client_website[0])
            else:
                raise ValidationError(
                    {"error": "Something is wrong(Website unavailable)"}
                )
        else:
            raise ValidationError({"error": "You are not allowed(Origin unavailable)"})

        return serializer.save()

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            if SETTINGS["ONE_DEVICE_PER_USER"] and self.request.data.get(
                "active", False
            ):
                FCMTokenDevice.objects.filter(user=self.request.user).update(
                    active=False
                )

            return serializer.save(user=self.request.user)
        return serializer.save()


class AuthorizedMixin(object):
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        # filter all devices to only those belonging to the current user
        return self.queryset.filter(user=self.request.user)
