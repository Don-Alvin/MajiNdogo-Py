# Maji Ndogo Project

## Introduction

Welcome to the Maji Ndogo project! This initiative aims to automate farming in Maji Ndogo, a region with diverse and challenging agricultural landscapes. Our mission is to make informed decisions about where and what to plant, considering factors like rainfall, soil type, climate, and more.

Our analysis forms the foundation of this automation project. By examining variables such as soil fertility, climate conditions, and geographical data, we can recommend the best locations for different crops. Think of it as solving a complex puzzle—each piece of data is crucial to seeing the bigger picture.

We'll begin by importing our dataset from an SQLite database, which is split into multiple tables. Unlike tools like Power BI or SQL, Python data analysis typically happens in a single DataFrame.

Once the data is ready, we'll dive deep to uncover patterns and correlations, guiding us toward the best farming practices for Maji Ndogo.

Let's get started and make a real difference!

## Data Dictionary

### 1. Geographic Features

- **Field_ID**: Unique identifier for each field (BigInt)
- **Elevation**: Elevation above sea level in metres (Float)
- **Latitude**: Geographical latitude in degrees (Float)
- **Longitude**: Geographical longitude in degrees (Float)
- **Location**: Province the field is in (Text)
- **Slope**: Slope of the land (Float)

### 2. Weather Features

- **Field_ID**: Corresponding field identifier (BigInt)
- **Rainfall**: Rainfall in mm (Float)
- **Min_temperature_C**: Average minimum temperature in Celsius (Float)
- **Max_temperature_C**: Average maximum temperature in Celsius (Float)
- **Ave_temps**: Average temperature in Celsius (Float)

### 3. Soil and Crop Features

- **Field_ID**: Corresponding field identifier (BigInt)
- **Soil_fertility**: Soil fertility (0 = infertile, 1 = very fertile) (Float)
- **Soil_type**: Type of soil (Text)
- **pH**: Soil pH level (Float)

### 4. Farm Management Features

- **Field_ID**: Corresponding field identifier (BigInt)
- **Pollution_level**: Pollution (0 = unpolluted, 1 = very polluted) (Float)
- **Plot_size**: Plot size in hectares (Float)
- **Chosen_crop**: Crop chosen for cultivation (Text)
- **Annual_yield**: Total annual yield (Float)
- **Standard_yield**: Standardised yield per crop (Float)

#### Average Yield (tons/Ha) per Crop Type

| Crop    | Yield (tons/Ha) |
|---------|-----------------|
| Coffee  | 1.5             |
| Wheat   | 3               |
| Rice    | 4.5             |
| Maize   | 5.5             |
| Tea     | 1.2             |
| Potato  | 20              |
| Banana  | 30              |
| Cassava | 13              |

---

## Getting Started: Importing Data

The dataset is stored in an SQLite database (`Maji_Ndogo_farm_survey.db`) with multiple tables. To prepare for analysis:

1. **Join tables**: Use SQL to join tables on the common key `Field_ID`.
2. **Import to DataFrame**: Load the joined data into a single DataFrame in Python.
3. **Clean and reshape**: Tidy up the data, handle missing values, and reshape as needed.

This process sets the stage for all subsequent analyses and insights.

---

Let's dive into the data and uncover the stories it has to tell!

Karibu Sana.