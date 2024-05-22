import unittest
from database_setup.setup_cassandra import setup_cassandra

class TestCassandraSetup(unittest.TestCase):
    def test_setup(self):
        result = setup_cassandra()
        self.assertTrue(result)
