
# Terp Transit: Shuttle-UM Operations Data Warehouse

## Project Overview
The **Terp Transit** project is an end-to-end data integration and warehousing solution designed to analyze the efficiency of the University of Maryland (UMD) Shuttle-UM system. By ingesting, cleansing, and transforming disparate data sources into a centralized dimensional model, this project investigates how external factors—specifically NOAA weather conditions and campus athletic/social events—impact bus arrival times, route efficiency, and passenger capacity.

This project was developed as a comprehensive exercise in data engineering, ETL pipeline development, and dimensional data modeling.

## Architecture & Technologies
*   **Data Engineering:** Python, PySpark, Pandas
*   **Data Warehousing:** SQL (SSMS, SSIS), Dimensional Data Modeling (Star Schema)
*   **Development Environment:** Jupyter Notebooks
*   **Concepts Applied:** Data staging, cleansing, transformation, integration, and governance.

## Data Sources
This data warehouse integrates three primary datasets into a unified dimension table:
1.  **Shuttle-UM Transit Logs:** Historical trip data, timestamps, route IDs, and capacity metrics.
2.  **NOAA Weather Data:** Historical meteorological data (e.g., precipitation, temperature) to analyze the impact of adverse weather on transit delays.
3.  **UMD Campus Event Calendars:** Schedules for major university events (e.g., athletic games) to analyze localized traffic spikes and ridership demand.

## Dimensional Model (Star Schema)
The architecture follows a Star Schema design to optimize analytical querying:
*   **Fact Table:** `Fact_Transit_Operations` (Records individual trip metrics, delay durations, and capacity flags).
*   **Dimension Tables:**
    *   `Dim_Date` / `Dim_Time`
    *   `Dim_Route` (Shuttle-UM specific routes and stops)
    *   `Dim_Weather` (Categorized NOAA weather conditions)
    *   `Dim_Event` (Campus event types and locations)

## Repository Structure
├── data/
│   ├── raw/               # Raw transit, weather, and event CSVs
│   ├── processed/         # Cleaned and merged datasets ready for loading
├── notebooks/
│   ├── 01_data_ingestion.ipynb       # Scripts for API calls and raw data loading
│   ├── 02_data_cleansing.ipynb       # Handling nulls, deduplication, and staging
│   ├── 03_dimensional_modeling.ipynb # Merging datasets into the star schema
├── src/
│   ├── etl_pipeline.py    # Core ETL pipeline scripts (PySpark/Python)
│   ├── schema_setup.sql   # SQL scripts for creating Fact and Dimension tables
├── docs/
│   ├── project_proposal.pdf
│   └── data_dictionary.md
└── README.md

## Key Analytical Queries
The warehouse is structured to efficiently answer questions such as:
1.  *How do heavy precipitation events correlate with average delay times on the 104 College Park Metro route?*
2.  *Which specific campus events generate the highest capacity strain on the transit system?*
3.  *What is the optimal bus allocation strategy during simultaneous adverse weather and major sporting events?*

## Contributors
*   Chenyue Pan
*   Purav Jay Patel
*   Nisank Arnav Arunkumar
