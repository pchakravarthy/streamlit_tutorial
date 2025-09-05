import streamlit as st
import pandas as pd

st.set_page_config(page_title="Power Plants in Europe", layout="wide")

st.title("Power Plants in Europe")

@st.cache_data
def load_powerplants():
    url = "https://raw.githubusercontent.com/PyPSA/powerplantmatching/master/powerplants.csv"
    return pd.read_csv(url, index_col=0)

ppl = load_powerplants()

with st.sidebar:
    st.title("Data Science for Energy System Modelling")
    st.markdown(":+1: This notebook introduces you to the `streamlit` library.")
    tech = st.selectbox(
        "Select a technology",
        ppl.Fueltype.unique(),
    )
    start, end = st.slider(
        "Range of commissioning years", 1900, 2022, (1900, 2022), step=1, help="Pick years!"
    )

hover_data = ['Name', 'Fueltype', 'Technology', "Capacity", 'Efficiency', 'DateIn']
df = ppl.query("Fueltype == @tech and DateIn >= @start and DateIn <= @end")