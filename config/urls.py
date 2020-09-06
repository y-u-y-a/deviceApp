from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
# app views
from device.views import DeviceViewSet
from user.views import UserViewSet


# create router instance
router = routers.DefaultRouter()
router.register('devices', DeviceViewSet) # 'api/devices/'
router.register('users', UserViewSet) # 'api/users/'


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
