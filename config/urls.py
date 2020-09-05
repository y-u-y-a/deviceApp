from django.contrib import admin
from django.urls import path
from django.conf.urls import include # 追加

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),
    # 追加
    path('api/device/', include('device.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
