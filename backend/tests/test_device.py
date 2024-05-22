# test_device.py

from django.test import TestCase
from backend.models.device import Device

class DeviceTestCase(TestCase):
    def setUp(self):
        Device.objects.create(name="Sensor1", type="Temperature", location="Room1", status="Active")
    
    def test_device_creation(self):
        sensor = Device.objects.get(name="Sensor1")
        self.assertEqual(sensor.type, "Temperature")
