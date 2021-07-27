from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.api.mixins import DeviceViewSetMixin
from core.models import FCMTokenDevice
from core.api.serializers import FCMTokenDeviceSerializer
from core.api.mixins import AuthorizedMixin

# ViewSets
class FCMTokenDeviceViewSet(DeviceViewSetMixin, ModelViewSet):
    queryset = FCMTokenDevice.objects.all()
    serializer_class = FCMTokenDeviceSerializer


class FCMTokenDeviceCreateOnlyViewSet(
    DeviceViewSetMixin, CreateModelMixin, GenericViewSet
):
    queryset = FCMTokenDevice.objects.all()
    serializer_class = FCMTokenDeviceSerializer


class FCMTokenDeviceAuthorizedViewSet(AuthorizedMixin, FCMTokenDeviceViewSet):
    pass
