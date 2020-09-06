from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings
# viewsets
from device.views import DeviceViewSet


# create router instance
router = routers.DefaultRouter()
router.register('devices', DeviceViewSet) # 'api/device/'


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
