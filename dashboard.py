import pandas as pd
import streamlit as st

st.title("🇧🇩 CPTU Tender Dashboard")

df = pd.read_csv("data.csv")

st.dataframe(df)

agency = st.selectbox("Filter by Agency", ["All"] + sorted(df["Agency"].unique()))

if agency != "All":
    df = df[df["Agency"] == agency]

st.write(df)
