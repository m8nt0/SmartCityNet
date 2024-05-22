# test_network.py

from django.test import TestCase
from backend.models.network import Network

class NetworkTestCase(TestCase):
    def setUp(self):
        Network.objects.create(name="Network1", topology="Topology1", status="Operational")
    
    def test_network_creation(self):
        network = Network.objects.get(name="Network1")
        self.assertEqual(network.status, "Operational")
