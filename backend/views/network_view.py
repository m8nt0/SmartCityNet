# network_view.py

from rest_framework import viewsets
from backend.models.network import Network
from backend.serializers.network_serializer import NetworkSerializer

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
