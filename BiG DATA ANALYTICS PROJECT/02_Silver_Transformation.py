# Databricks notebook source
from pyspark.sql.functions import col, get_json_object, explode, from_json
from pyspark.sql.types import *

print("Starting the Silver sorting robot...\n")

# --- 1. SORTING THE WEATHER DATA ---
print("Opening Weather bags...")
df_bronze_weather = spark.read.table("bronze_weather")

# We pluck out just the city name, the weather condition (like "Rain"), and the temperature
df_silver_weather = df_bronze_weather.select(
    col("ingestion_timestamp"),
    get_json_object(col("raw_json"), "$.name").alias("city"),
    get_json_object(col("raw_json"), "$.weather[0].main").alias("weather_condition"),
    get_json_object(col("raw_json"), "$.main.temp").cast("float").alias("temp_kelvin")
)

# The API gives us temperature in Kelvin. Let's make the robot convert it to Fahrenheit!
df_silver_weather = df_silver_weather.withColumn(
    "temp_f", ((col("temp_kelvin") - 273.15) * 1.8) + 32
).drop("temp_kelvin") # Drop the kelvin column to keep it clean

df_silver_weather.write.format("delta").mode("overwrite").saveAsTable("silver_weather")
print("✅ Weather sorted!")


# --- 2. SORTING THE TRANSIT DATA ---
print("Opening Transit bags...")
df_bronze_transit = spark.read.table("bronze_transit")

# The transit bag has a list (array) of incidents. We define a "Schema" to tell the robot what the list looks like.
schema_incidents = ArrayType(StructType([
    StructField("IncidentType", StringType(), True),
    StructField("Description", StringType(), True),
    StructField("LinesAffected", StringType(), True)
]))

# We open the list, and use 'explode' to give every single incident its own row
df_silver_transit = df_bronze_transit.withColumn(
    "incidents_array", 
    from_json(get_json_object(col("raw_json"), "$.Incidents"), schema_incidents)
).select("ingestion_timestamp", explode(col("incidents_array")).alias("incident")) \
.select(
    "ingestion_timestamp",
    col("incident.IncidentType").alias("incident_type"),
    col("incident.Description").alias("description"),
    col("incident.LinesAffected").alias("lines_affected")
)

df_silver_transit.write.format("delta").mode("overwrite").saveAsTable("silver_transit")
print("✅ Transit sorted!")


# --- 3. SORTING THE EVENTS DATA ---
print("Opening Events bags...")
df_bronze_events = spark.read.table("bronze_events")

# The events bag also has a list. We define the blueprint for the event name and date.
schema_events = ArrayType(StructType([
    StructField("name", StringType(), True),
    StructField("dates", StructType([
        StructField("start", StructType([
            StructField("localDate", StringType(), True),
            StructField("localTime", StringType(), True)
        ]))
    ]))
]))

df_silver_events = df_bronze_events.withColumn(
    "events_array",
    from_json(get_json_object(col("raw_json"), "$._embedded.events"), schema_events)
).select("ingestion_timestamp", explode(col("events_array")).alias("event")) \
.select(
    "ingestion_timestamp",
    col("event.name").alias("event_name"),
    col("event.dates.start.localDate").alias("event_date"),
    col("event.dates.start.localTime").alias("event_time")
)

df_silver_events.write.format("delta").mode("overwrite").saveAsTable("silver_events")
print("✅ Events sorted!")

print("\nAll done! The Silver tables are beautifully organized.")