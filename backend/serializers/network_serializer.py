# network_serializer.py

from rest_framework import serializers
from backend.models.network import Network

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'
