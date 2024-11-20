# Databricks notebook source
import requests
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("API Data Retrieval").getOrCreate()

# Example API request
url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    # Get the response data
    data = response.json()

    # Store the data in a Databricks table
    # Replace 'table_name' with the actual table name in Databricks
    spark_df = spark.createDataFrame(data)
    spark_df.write.format("delta").mode("overwrite").saveAsTable("table_name")
    print(data)
else:
    print("Error: Failed to retrieve data from the API.")
