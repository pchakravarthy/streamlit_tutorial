import streamlit as st
import pandas as pd
from data.modis_aqua_data import load_nasa_modis_images
from PIL import Image

st.set_page_config(page_title="MODIS_NASA", layout="wide")

st.title("MODIS_NASA")

nasa_df = load_nasa_modis_images()

# st.dataframe(nasa_df[['start_date', 'filename']])

# st.write(nasa_df["start_date"])

# Extract the year into a new Series
years_only_df = nasa_df['start_date'].dt.year.unique()

with st.sidebar:
    st.title("Yearly Images")
    # st.write(nasa_df["start_date"])
    start_dates = st.selectbox("Select a year", sorted(years_only_df))
    # st.write(start_dates)
    # start, end = st.slider(
    #     "Range of commissioning years", 1900, 2022, (1900, 2022), step=1, help="Pick years!"
    # )
# st.write(start_dates)
# st.write(type(start_dates))

filtered_df = nasa_df[nasa_df['start_date'].dt.year == start_dates]

with st.spinner("Generating Ocean Floor"):
    for image in filtered_df['image_plt']:
        st.pyplot(image)

# st.table(nasa_images)

# image_data = load_nasa_modis_images()[0]
# image_path = load_nasa_modis_images()[1]
# image = Image.open(image_path) 

# st.image(image, caption='MODIS_NASA', width=400) 
