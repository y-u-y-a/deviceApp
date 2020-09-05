from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from device.views import DeviceViewSet


# ルーティングを定義・追加
router = routers.DefaultRouter()
# 'api/devices/'
router.register('devices', DeviceViewSet)


urlpatterns = [
    # 何もない場合はrouterを参照
    path('', include(router.urls))
]
