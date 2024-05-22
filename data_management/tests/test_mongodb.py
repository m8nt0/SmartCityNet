import unittest
from database_setup.setup_mongodb import setup_mongodb

class TestMongoDBSetup(unittest.TestCase):
    def test_setup(self):
        result = setup_mongodb()
        self.assertTrue(result)
