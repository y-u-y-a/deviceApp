from django.http import HttpResponse
from rest_framework import viewsets

from core.models import User
from core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
