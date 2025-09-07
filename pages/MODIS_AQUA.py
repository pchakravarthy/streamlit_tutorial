import streamlit as st
import pandas as pd
from data.modis_aqua_data import load_nasa_modis_images
from PIL import Image

st.set_page_config(page_title="MODIS_NASA", layout="wide")

st.title("MODIS_NASA")

nasa_df = load_nasa_modis_images()

st.dataframe(nasa_df[['start_date', 'filename']])

with st.sidebar:
    st.title("Yearly Images")
    start_dates = st.selectbox("Select a year", nasa_df['start_date'].unique())
    # start, end = st.slider(
    #     "Range of commissioning years", 1900, 2022, (1900, 2022), step=1, help="Pick years!"
    # )


for image in nasa_df['image_plt']:
    st.pyplot(image)

# st.table(nasa_images)

# image_data = load_nasa_modis_images()[0]
# image_path = load_nasa_modis_images()[1]
# image = Image.open(image_path) 

# st.image(image, caption='MODIS_NASA', width=400) 
