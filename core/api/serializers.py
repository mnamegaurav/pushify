from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    Serializer,
    CurrentUserDefault,
)

from core.models import FCMTokenDevice
from core.api.mixins import UniqueRegistrationSerializerMixin, DeviceSerializerMixin


# Serializers
class FCMTokenDeviceSerializer(ModelSerializer, UniqueRegistrationSerializerMixin):
    class Meta(DeviceSerializerMixin.Meta):
        model = FCMTokenDevice

        extra_kwargs = {"id": {"read_only": True, "required": False}}
        extra_kwargs.update(DeviceSerializerMixin.Meta.extra_kwargs)
