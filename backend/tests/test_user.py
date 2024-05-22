# test_user.py

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="user1", password="password")
    
    def test_user_creation(self):
        user = User.objects.get(username="user1")
        self.assertTrue(user.check_password("password"))
