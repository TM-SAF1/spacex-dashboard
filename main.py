import streamlit as st
import pandas as pd
from spacex_api import get_all_launches
import plotly.express as px

# Fetch all launches
launches = get_all_launches()

# Extract relevant info
data = []
for l in launches:
    data.append({
        "Name": l.get("name"),
        "Date": l.get("date_utc"),
        "Success": l.get("success"),
        "Rocket": l.get("rocket")
    })

# Create DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Save CSV
df.to_csv("spacex_launches.csv", index=False)

# Streamlit UI
st.title("🚀 SpaceX Launch Dashboard")
st.write("All launches data saved to `spacex_launches.csv`")

# Success / Failed count
success_count = df['Success'].value_counts()
st.write("### Launch Outcomes")
st.write(success_count)

# Plot graph
fig = px.histogram(df, x="Date", color="Success", 
                   title="SpaceX Launch Success / Failures Over Time",
                   color_discrete_map={True: "green", False: "red"})
st.plotly_chart(fig)
