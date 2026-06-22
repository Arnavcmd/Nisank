# Databricks notebook source
import requests
import json
from pyspark.sql.functions import current_timestamp

# --- 1. YOUR SECRET PASSWORDS ---
weather_key = "1df290606f285a3fd44726ab2611f1de"
tm_key = "IuBt8zVKJ1H6OaBADJSS8wvlIDEXYtiq"
wmata_key = "58b0d6a3d6004462933c184e7c7be5e3"

print("Starting the serverless robot helper... catching raw packages!\n")

# --- 2. TUBE 1: OPENWEATHERMAP ---
print("Fetching Weather...")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Washington,US&appid={weather_key}"
w_response = requests.get(weather_url)

if w_response.status_code == 200:
    # Convert the response to a single raw string
    raw_weather_str = json.dumps(w_response.json())
    
    # Put that string inside a neat Spark DataFrame row
    df_weather = spark.createDataFrame([(raw_weather_str,)], ["raw_json"]) \
                      .withColumn("ingestion_timestamp", current_timestamp())
    
    # Save directly to the Delta table
    df_weather.write.format("delta").mode("append").saveAsTable("bronze_weather")
    print("✅ Weather dumped in Bronze Box!")
else:
    print(f"❌ Weather tube jammed. Error: {w_response.status_code}")


# --- 3. TUBE 2: TICKETMASTER ---
print("\nFetching Events...")
tm_url = f"https://app.ticketmaster.com/discovery/v2/events.json?city=Washington&apikey={tm_key}"
tm_response = requests.get(tm_url)

if tm_response.status_code == 200:
    raw_events_str = json.dumps(tm_response.json())
    
    df_events = spark.createDataFrame([(raw_events_str,)], ["raw_json"]) \
                     .withColumn("ingestion_timestamp", current_timestamp())
                     
    df_events.write.format("delta").mode("append").saveAsTable("bronze_events")
    print("✅ Events dumped in Bronze Box!")
else:
    print(f"❌ Event tube jammed. Error: {tm_response.status_code}")


# --- 4. TUBE 3: WMATA TRANSIT ---
print("\nFetching Transit Issues...")
wmata_url = "https://api.wmata.com/Incidents.svc/json/Incidents"
wmata_headers = {"api_key": wmata_key}
wmata_response = requests.get(wmata_url, headers=wmata_headers)

if wmata_response.status_code == 200:
    raw_transit_str = json.dumps(wmata_response.json())
    
    df_transit = spark.createDataFrame([(raw_transit_str,)], ["raw_json"]) \
                      .withColumn("ingestion_timestamp", current_timestamp())
                      
    df_transit.write.format("delta").mode("append").saveAsTable("bronze_transit")
    print("✅ Transit dumped in Bronze Box!")
else:
    print(f"❌ Transit tube jammed. Error: {wmata_response.status_code}")

print("\nAll done! The Bronze Toybox is full with clean, raw packages.")