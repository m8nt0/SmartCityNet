import unittest
from data_processing.spark_job import run_spark_job

class TestSparkJob(unittest.TestCase):
    def test_spark_job(self):
        result = run_spark_job()
        self.assertEqual(result, 'success')
