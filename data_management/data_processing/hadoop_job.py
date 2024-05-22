# hadoop_job.py

from pyhdfs import HdfsClient

def run_hadoop_job():
    client = HdfsClient(hosts='localhost:50070', user_name='hadoop')
    client.mkdirs('/user/hadoop/input')
    # Add more Hadoop job code here
