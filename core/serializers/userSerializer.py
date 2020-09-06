from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        # 公開する値
        model = User
        fields = ['id', 'name', 'email']
