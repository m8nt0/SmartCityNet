# device_serializer.py

from rest_framework import serializers
from backend.models.device import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
