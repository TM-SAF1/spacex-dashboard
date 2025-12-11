import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="SpaceX Launch Dashboard", layout="wide")
st.title("🚀 SpaceX Launch Dashboard")
st.write("Live data fetched directly from SpaceX API. No CSVs needed.")

# Fetch live data
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
df = pd.DataFrame(response.json())

# Convert dates
df["date_utc"] = pd.to_datetime(df["date_utc"])
df["success"] = df["success"].fillna(False)  # fill missing success info

# Layout
col1, col2 = st.columns(2)

# Success vs Failure pie chart
with col1:
    st.subheader("Success vs Failure")
    fig1 = px.pie(
        df,
        names="success",
        title="Launch Outcome Breakdown",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

# Launches timeline
with col2:
    st.subheader("Launches Timeline")
    fig2 = px.scatter(
        df,
        x="date_utc",
        y=df.index,  # or "name" if you prefer labels
        color="success",
        title="Launches Over Time",
        hover_data=["name", "rocket"]
    )
    st.plotly_chart(fig2, use_container_width=True)

# Full table
st.subheader("Launch Data Table")
st.dataframe(df)

