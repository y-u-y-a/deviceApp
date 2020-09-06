from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from core.models import Device
from core.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


    def post(self, request, *args, **kwargs):
        title = request.data['title']
        image = request.data['image']

        # create
        Device.create(title=title, image=image)
        message = 'create new device'
        return HttpResponse(
            {'message': message},
            status=200
        )
