from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


    def post(self, request, *args, **kwargs):
        title = request.data['title']
        image = request.data['image']

        # DB登録
        Device.create(title=title, image=image)
        message = 'create new device'
        return HttpResponse(
            {'message': message},
            status=200
        )
