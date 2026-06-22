# Databricks notebook source
from pyspark.sql.functions import col, to_date

print("Starting the Gold assembly robot...\n")

# --- 1. GRAB THE SILVER TABLES ---
df_weather = spark.read.table("silver_weather")
df_transit = spark.read.table("silver_transit")
df_events = spark.read.table("silver_events")

# --- 2. CREATE A COMMON PUZZLE PIECE (THE DATE) ---
# We need to make sure all three tables have an exact "Date" column to snap them together.
# For Weather and Transit, we extract the date from when we grabbed it (today).
df_weather_clean = df_weather.withColumn("join_date", to_date(col("ingestion_timestamp"))).drop("ingestion_timestamp")
df_transit_clean = df_transit.withColumn("join_date", to_date(col("ingestion_timestamp"))).drop("ingestion_timestamp")

# For Events, we use the actual date of the event (which the API gave us as a string).
df_events_clean = df_events.withColumn("join_date", to_date(col("event_date"))).drop("ingestion_timestamp", "event_date")

print("Puzzle pieces created. Snapping tables together...")

# --- 3. THE GRAND JOIN ---
# We start with Transit, glue on the Weather for that day, and then glue on the Events for that day.
df_gold = df_transit_clean.join(df_weather_clean, "join_date", "left") \
                          .join(df_events_clean, "join_date", "left")

# --- 4. SAVE TO THE GOLD BOX ---
df_gold.write.format("delta").mode("overwrite").saveAsTable("gold_transit_vulnerability")

print("✅ Gold Master Table created successfully!")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Let's see what the weather and local events look like for every transit delay!
# MAGIC SELECT 
# MAGIC     join_date as Date,
# MAGIC     incident_type as Transit_Issue,
# MAGIC     lines_affected as Metro_Lines,
# MAGIC     weather_condition as Weather,
# MAGIC     ROUND(temp_f, 1) as Temp_Fahrenheit,
# MAGIC     event_name as Local_Event
# MAGIC FROM gold_transit_vulnerability
# MAGIC LIMIT 15;