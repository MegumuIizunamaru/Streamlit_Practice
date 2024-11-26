import streamlit as st
import pandas as pd
import numpy as np

# Title of the dashboard
st.title("Tengu Population Analysis")

# Adding a sidebar
st.sidebar.header("Filters")
region = st.sidebar.selectbox("Select Region", ["North", "South", "East", "West"])

# Generate dummy data
data = {
    "Region": ["North", "South", "East", "West"],
    "Population": [100, 200, 150, 180],
    "Happiness Score": [70, 60, 80, 65],
}
df = pd.DataFrame(data)

# Filter data by region
filtered_data = df[df["Region"] == region]

# Show data
st.subheader(f"Data for {region} Region")
st.write(filtered_data)

# Add a chart
st.bar_chart(df.set_index("Region")["Population"])

# Add some interactivity
if st.button("Show Fun Fact"):
    st.write(f"The happiest region is {df.loc[df['Happiness Score'].idxmax(), 'Region']}!")

