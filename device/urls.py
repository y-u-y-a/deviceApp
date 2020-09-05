from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from device.views import DeviceViewSet


# Define routings
router = routers.DefaultRouter()
# 'api/device/'
router.register('', DeviceViewSet)


urlpatterns = [
    path('', include(router.urls))
]
