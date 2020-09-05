# シリアライザーとは？
# フロントに渡したいデータなどを制限
from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # モデルを指定
        model = Device
        # 後悔する値を指定
        fields = ['id', 'title', 'image']
