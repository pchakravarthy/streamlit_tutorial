import streamlit as st
import pandas as pd
from data.powerplant_utils import load_powerplants, filter_powerplants

st.set_page_config(page_title="Capacity by Country", layout="wide")

st.title("Capacity by Country")


ppl = load_powerplants()

with st.sidebar:
    st.title("Bar chart")
    tech = st.selectbox("Select a technology", ppl.Fueltype.unique())
    start, end = st.slider(
        "Range of commissioning years", 1900, 2022, (1900, 2022), step=1, help="Pick years!"
    )

df = filter_powerplants(ppl, tech, start, end)

st.subheader("Capacity by Country")
if not df.empty:
    bar_data = df.groupby("Country")[["Capacity"]].sum().sort_values("Capacity", ascending=False)
    st.bar_chart(bar_data)
else:
    st.info("No data to display for bar chart.")
