# MajiNdogo Data Pipeline

This project implements a data pipeline for ingesting, transforming, cleaning, and preparing agricultural data for analysis. The pipeline also includes validation tests to ensure data quality.

## Data Pipeline Steps

1. **Ingest Data**  
    - Load raw data from CSV files and other sources.

2. **Transform Data**  
    - Convert ingested data into pandas DataFrames.
    - Join and merge datasets as needed.

3. **Clean Data**  
    - Handle missing values, outliers, and inconsistent data.
    - Standardize formats and data types.

4. **Prepare Data for Analysis**  
    - Feature engineering and selection.
    - Normalize and encode categorical variables.

5. **Validate Data**  
    - Run tests to ensure data integrity and correctness.

---

## Data Dictionary

### Geographic Features

| Field         | Type    | Description                                                      |
|---------------|---------|------------------------------------------------------------------|
| Field_ID      | BigInt  | Unique identifier for each field                                 |
| Elevation     | Float   | Elevation above sea level (metres)                               |
| Latitude      | Float   | Geographical latitude (degrees)                                  |
| Longitude     | Float   | Geographical longitude (degrees)                                 |
| Location      | Text    | Province the field is in                                         |
| Slope         | Float   | Slope of the land                                                |

### Weather Features

| Field             | Type    | Description                                                  |
|-------------------|---------|--------------------------------------------------------------|
| Field_ID          | BigInt  | Corresponding field identifier                               |
| Rainfall          | Float   | Rainfall in mm                                               |
| Min_temperature_C | Float   | Average minimum temperature (°C)                             |
| Max_temperature_C | Float   | Average maximum temperature (°C)                             |
| Ave_temps         | Float   | Average temperature (°C)                                     |

### Soil and Crop Features

| Field         | Type    | Description                                                      |
|---------------|---------|------------------------------------------------------------------|
| Field_ID      | BigInt  | Corresponding field identifier                                   |
| Soil_fertility| Float   | Soil fertility (0 = infertile, 1 = very fertile)                 |
| Soil_type     | Text    | Type of soil                                                     |
| pH            | Float   | Soil pH level                                                    |

### Farm Management Features

| Field           | Type    | Description                                                    |
|-----------------|---------|----------------------------------------------------------------|
| Field_ID        | BigInt  | Corresponding field identifier                                 |
| Pollution_level | Float   | Pollution level (0 = unpolluted, 1 = very polluted)            |
| Plot_size       | Float   | Plot size (Ha)                                                 |
| Chosen_crop     | Text    | Crop chosen for cultivation                                    |
| Annual_yield    | Float   | Total annual yield from the field                              |
| Standard_yield  | Float   | Standardized yield per crop                                    |

### Weather Station Data (CSV)

| Field              | Type   | Description                                                  |
|--------------------|--------|--------------------------------------------------------------|
| Weather_station_ID | Int    | Weather station identifier                                   |
| Message            | Str    | Sensor-captured weather data (text message)                  |

### Weather Data Field Mapping (CSV)

| Field              | Type   | Description                                                  |
|--------------------|--------|--------------------------------------------------------------|
| Field_ID           | Int    | Field identifier (join key)                                  |
| Weather_station_ID | Int    | Closest weather station identifier                           |

