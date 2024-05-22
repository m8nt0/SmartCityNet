# device_view.py

from rest_framework import viewsets
from backend.models.device import Device
from backend.serializers.device_serializer import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
