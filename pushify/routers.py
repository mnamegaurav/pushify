from rest_framework.routers import DefaultRouter

from core.api.viewsets import (
    FCMTokenDeviceViewSet,
    FCMTokenDeviceAuthorizedViewSet,
    FCMTokenDeviceCreateOnlyViewSet,
)

router = DefaultRouter()
router.register(
    "fcm/device/create", FCMTokenDeviceCreateOnlyViewSet, basename="fcm-token-device"
)
# router.register("fcm/devices", FCMTokenDeviceViewSet, basename="fcm-token-devices")
