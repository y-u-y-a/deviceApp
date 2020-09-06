from rest_framework import serializers
from core.models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        # 公開する値
        model = Device
        fields = ['id', 'title', 'image']
