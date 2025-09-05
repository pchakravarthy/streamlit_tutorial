import pandas as pd
import streamlit as st

@st.cache_data
def load_powerplants():
    url = "https://raw.githubusercontent.com/PyPSA/powerplantmatching/master/powerplants.csv"
    return pd.read_csv(url, index_col=0)

def filter_powerplants(ppl, tech, start, end):
    return ppl.query("Fueltype == @tech and DateIn >= @start and DateIn <= @end")
