import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px

# Set page config
st.set_page_config(page_title="SafeRoads India", layout="wide")

# DB path
DB_PATH = os.path.join("db", "road_accidents.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Connect to DB
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM road_accidents", conn)

st.title("🚧 SafeRoads India: Road Accidents Analysis (2020)")
st.markdown("An interactive dashboard to analyze 3-year trends in Indian road accidents and fatalities.")

# Filter by state
state_list = sorted(df["state"].unique())
selected_state = st.selectbox("Select a State", state_list)

filtered_df = df[df["state"] == selected_state]

# Show data preview
with st.expander(f"🔍 Raw Data for {selected_state}"):
    st.dataframe(filtered_df)

# Grouped bar chart for accident vs fatality
st.subheader(f"📊 Accident & Fatality Trends in {selected_state}")
bar_df = filtered_df.groupby("district")[["accidents_total", "fatalities_total"]].sum().reset_index()

fig1 = px.bar(
    bar_df,
    x="district",
    y=["accidents_total", "fatalities_total"],
    title="District-wise Accidents vs Fatalities",
    barmode="group"
)
st.plotly_chart(fig1, use_container_width=True)

# Top dangerous locations
st.subheader("🚨 Top 10 Most Accident-Prone Locations")
top_locations = filtered_df.sort_values("accidents_total", ascending=False).head(10)
st.table(top_locations[["district", "location", "accidents_total", "fatalities_total"]])

# State-level comparison
st.subheader("📈 Statewise Total Accidents vs Fatalities")
state_summary = df.groupby("state")[["accidents_total", "fatalities_total"]].sum().reset_index().sort_values("accidents_total", ascending=False)

fig2 = px.bar(
    state_summary,
    x="state",
    y=["accidents_total", "fatalities_total"],
    title="Total Accidents and Fatalities by State",
    barmode="group"
)
st.plotly_chart(fig2, use_container_width=True)

# Close connection
conn.close()
