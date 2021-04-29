from rest_framework.routers import DefaultRouter

from fcm_django.api.rest_framework import FCMDeviceViewSet, FCMDeviceAuthorizedViewSet

router = DefaultRouter()
router.register("fcm/devices", FCMDeviceViewSet, basename="fcm-device")
