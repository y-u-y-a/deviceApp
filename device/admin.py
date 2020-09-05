from django.contrib import admin


from .models import Device


# 管理画面に扱うモデルを追加
admin.site.register(Device)
