import pandas as pd
import sqlite3
import os

# File paths
CSV_PATH = os.path.join("data", "RA2020_A52.csv")
DB_PATH = os.path.join("db", "road_accidents.db")

# Ensure db folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Load dataset with encoding handling
df = pd.read_csv(CSV_PATH, encoding='ISO-8859-1')

# Show all columns to understand structure
print("🔍 Columns in dataset:")
print(df.columns)

# Rename and clean columns
df = df.rename(columns={
    'State': 'state',
    'Name of District (Traffic unit)': 'district',
    'Name of Location Place': 'location',
    'Numbers of Accidents - 2016': 'accidents_2016',
    'Numbers of Accidents - 2017': 'accidents_2017',
    'Numbers of Accidents - 2018': 'accidents_2018',
    'Numbers of Accidents - Total of all three years': 'accidents_total',
    'Numbers of Fatalities - 2016': 'fatalities_2016',
    'Numbers of Fatalities - 2017': 'fatalities_2017',
    'Numbers of Fatalities - 2018': 'fatalities_2018',
    'Numbers of Fatalities - Total of all three years': 'fatalities_total'
})

# Drop rows missing state or district
df.dropna(subset=["state", "district"], inplace=True)

# Create SQLite DB connection
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS road_accidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state TEXT,
    district TEXT,
    location TEXT,
    accidents_2016 INTEGER,
    accidents_2017 INTEGER,
    accidents_2018 INTEGER,
    accidents_total INTEGER,
    fatalities_2016 INTEGER,
    fatalities_2017 INTEGER,
    fatalities_2018 INTEGER,
    fatalities_total INTEGER
)
''')

# Insert selected columns
cols = ["state", "district", "location", "accidents_2016", "accidents_2017", "accidents_2018", 
        "accidents_total", "fatalities_2016", "fatalities_2017", "fatalities_2018", "fatalities_total"]

df_to_insert = df[cols]

df_to_insert.to_sql('road_accidents', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("✅ ETL complete! Data inserted into database.")
