# spark_job.py

from pyspark.sql import SparkSession

def run_spark_job():
    spark = SparkSession.builder.appName("SmartCityNet").getOrCreate()
    df = spark.read.csv("hdfs://localhost:9000/user/hadoop/input")
    df.show()
    # Add more Spark job code here
