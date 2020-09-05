# シリアライザーとは？
# フロントに渡したいデータなどを制限
from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        # 公開する値
        model = Device
        fields = ['id', 'title', 'image']
