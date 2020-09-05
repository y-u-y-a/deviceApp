from rest_framework import routers
from django.urls import path
from django.conf.urls import include
# from device.views import DeviceViewSet


# ルーティングを定義・追加
router = routers.DefaultRouter()
# router.register('devices', DeviceViewSet) # 'api/devices/'の場合


urlpatterns = [
    # 何もない場合はrouterを参照
    path('', include(router.urls))
]
