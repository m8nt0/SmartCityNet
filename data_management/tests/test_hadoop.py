import unittest
from data_processing.hadoop_job import run_hadoop_job

class TestHadoopJob(unittest.TestCase):
    def test_hadoop_job(self):
        result = run_hadoop_job()
        self.assertEqual(result, 'success')
