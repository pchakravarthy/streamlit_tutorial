import io
import tempfile
import cartopy
from matplotlib import animation, pyplot as plt
import streamlit as st
import pandas as pd
from data.modis_aqua_data import load_nasa_modis_images
from PIL import Image

crs_proj = cartopy.crs.Robinson()
crs_data = cartopy.crs.PlateCarree()

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

with st.sidebar:
    st.title("fps")
    speed = st.selectbox("Select a speed", range(3, 30))


filtered_df = nasa_df[nasa_df['start_date'].dt.year == start_dates]
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(projection=crs_proj)
ax.coastlines()
chlor_data = list(filtered_df["chlor_data"])

def anim_func(i):
    ax.clear()
    
    im = chlor_data[i].plot(
        x="lon", y="lat", cmap="jet", ax=ax, robust=True, transform=crs_data, add_colorbar=False
    )
    ax.coastlines()
    ax.set_title(filtered_df.iloc[i]['filename'])
    return [im]

anim = animation.FuncAnimation(fig, anim_func, frames=len(chlor_data), interval = 500)
with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as temp_file:
    anim.save(temp_file.name, writer="pillow", fps = speed)
    temp_file.seek(0)
    gif_bytes = temp_file.read()

# buf = io.BytesIO()
# anim.save(buf, writer = "pillow")
# buf.seek(0)
st.image(gif_bytes, caption = "MODIS Animation (GIF)")



with st.spinner("Generating Ocean Floor"):
    for image in filtered_df['image_plt']:
        st.pyplot(image)


# st.table(nasa_images)

# image_data = load_nasa_modis_images()[0]
# image_path = load_nasa_modis_images()[1]
# image = Image.open(image_path) 

# st.image(image, caption='MODIS_NASA', width=400) 


