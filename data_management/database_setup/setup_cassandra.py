# setup_cassandra.py

from cassandra.cluster import Cluster

def setup_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute("CREATE KEYSPACE IF NOT EXISTS smartcitynet WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};")
    # Add more Cassandra setup code here
