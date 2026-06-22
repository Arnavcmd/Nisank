# Databricks notebook source
# MAGIC %md
# MAGIC System Architecture: The Urban Transit Vulnerability Matrix
# MAGIC 1. Project Overview
# MAGIC This data lake integrates three public APIs (WMATA Transit Incidents, OpenWeatherMap, and Ticketmaster Events) to analyze how environmental factors and major crowd events compound to stress transit infrastructure. The system employs a Medallion Architecture (Bronze, Silver, Gold) implemented via PySpark and Delta Lake, enabling cross-dataset temporal joins to identify correlations between weather, events, and transit delays.
# MAGIC
# MAGIC 2. Theoretical Grounding & Design Rationale
# MAGIC The design decisions in this pipeline are explicitly grounded in the concepts outlined in Martin Kleppmann's Designing Data-Intensive Applications.
# MAGIC
# MAGIC A. Batch vs. Stream Processing (Chapter 11)
# MAGIC Concept: The distinction between unbounded streams (data that is continuously generated) and bounded batches (processing a fixed set of data).
# MAGIC
# MAGIC Application: While WMATA transit incidents and weather are inherently continuous streams of events, Databricks Community Edition limitations necessitate a simulated micro-batch approach. We poll the APIs at scheduled intervals (batch processing) rather than maintaining a persistent streaming connection (e.g., via Kafka or Spark Structured Streaming). While true stream processing would reduce latency and allow for real-time delay alerting, our batch approach is highly appropriate and efficient for the system's primary goal: historical correlation analysis and aggregate reporting.
# MAGIC
# MAGIC B. Encoding and Evolution (Chapter 4)
# MAGIC Concept: Handling changes in data formats over time (schema evolution) to maintain forward and backward compatibility without breaking applications.
# MAGIC
# MAGIC Application: APIs are notoriously volatile; fields are frequently added or deprecated. To build a robust pipeline, the Bronze Layer utilizes a pure "Schema-on-Read" approach. Instead of attempting to parse the JSON during ingestion (which would cause pipeline failures if the API schema changed unexpectedly), we store the entire raw JSON payload as a single string column. Schema enforcement and type coercion are delayed until the Silver Layer, utilizing Delta Lake's capabilities to handle schema evolution gracefully, ensuring that historical raw data is never corrupted by upstream API changes.
# MAGIC
# MAGIC C. Partitioning and Skew (Chapter 6)
# MAGIC Concept: Breaking large datasets into smaller, manageable pieces (partitions) to distribute query load evenly across nodes.
# MAGIC
# MAGIC Application: In a production-scale version of this system, partitioning the Gold table by join_date (or year and month) is critical. Since transit analytics are heavily time-series based, partitioning by date ensures that queries analyzing specific timeframes (e.g., "delays during summer concert season") only scan the relevant partitions (partition pruning). We must acknowledge the trade-off here: partitioning solely by date could lead to "hot spots" if a specific day has an anomalously high volume of data (e.g., a massive storm causing thousands of transit events), which would require a compound partition key (e.g., date + transit_line) at terabyte scale.
# MAGIC
# MAGIC D. Storage Engines: Column-Oriented Storage (Chapter 3)
# MAGIC Concept: Storing data by columns rather than rows to dramatically improve the performance of analytical (OLAP) queries.
# MAGIC
# MAGIC Application: The raw data fetched from the APIs is row-oriented JSON. If we queried this raw data directly for our dashboards, the system would be forced to read every single attribute of every JSON object just to calculate an average temperature. By transforming the data and storing it in Delta tables (which are built on top of column-oriented Parquet files) in the Silver and Gold layers, our analytical queries only scan the specific columns requested (e.g., temp_f or incident_type). This reduces disk I/O, speeds up aggregations, and natively supports data compression.
# MAGIC
# MAGIC How to Submit Your Project
# MAGIC Ensure your workspace has the following notebooks in order:
# MAGIC
# MAGIC 00_README_Architecture (The Markdown document above)
# MAGIC
# MAGIC 01_Bronze_Ingestion
# MAGIC
# MAGIC 02_Silver_Transformation
# MAGIC
# MAGIC 03_Gold_Analytics
# MAGIC
# MAGIC At the top right of your Databricks screen, click the Share or Permissions button and invite your instructor using their email address, giving them "Can View" or "Can Run" access as required by the rubric.