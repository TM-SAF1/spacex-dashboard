import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SpaceX Launch Dashboard", layout="wide")

# Load CSV
df = pd.read_csv("spacex_data.csv")

st.title("🚀 SpaceX Launch Dashboard")
st.write("A simple dashboard showing launch outcomes using the public SpaceX API.")

# Layout
col1, col2 = st.columns(2)

# Success vs Failure pie chart
with col1:
    st.subheader("Success vs Failure")
    fig1 = px.pie(
        df,
        names="Success",
        title="Launch Outcome Breakdown",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

# Launches timeline
with col2:
    st.subheader("Launches Over Time")
    df["Date"] = pd.to_datetime(df["Date"])

    fig2 = px.scatter(
        df,
        x="Date",
        y="Rocket ID",
        color="Success",
        title="Launches Timeline",
        hover_data=["Name"]
    )
    st.plotly_chart(fig2, use_container_width=True)

# Full table
st.subheader("Launch Data Table")
st.dataframe(df)
