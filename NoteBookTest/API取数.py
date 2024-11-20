# Databricks notebook source
import requests

# Define the API endpoint
api_url = "https://api.example.com/data"

# Define the payload for the POST request
payload = {
    "param1": "value1",
    "param2": "value2"
}

# Make the POST request
response = requests.post(api_url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Get the response data
    data = response.json()

    # Store the data in a Databricks table
    # Replace 'table_name' with the actual table name in Databricks
    spark_df = spark.createDataFrame(data)
    spark_df.write.format("delta").mode("overwrite").saveAsTable("table_name")
else:
    print("Error: Failed to retrieve data from the API.")
