from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
# add views
from core.views import UserViewSet, DeviceViewSet


# create router instance
router = routers.DefaultRouter()
router.register('users', UserViewSet) # 'api/users/'
router.register('devices', DeviceViewSet) # 'api/devices/'


# Start
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
