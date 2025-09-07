from matplotlib import pyplot as plt
import cartopy
import earthaccess
import numpy as np
import xarray as xr
import os
import streamlit as st
import pandas as pd
from datetime import datetime

def get_image_data(full_path):
    dataset = xr.open_dataset(full_path)
    array = np.log10(dataset["chlor_a"])
    array.attrs.update(
        {
            "units": f'log10({dataset["chlor_a"].attrs["units"]})',
        }
    )
    crs_proj = cartopy.crs.Robinson()
    crs_data = cartopy.crs.PlateCarree()
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(projection=crs_proj)
    array.plot(x="lon", y="lat", cmap="jet", ax=ax, robust=True, transform=crs_data)
    ax.coastlines()
    ax.set_title(dataset.attrs["product_name"])
    return fig

# @st.cache_data
def load_nasa_modis_images():
    directory_path = "/Users/ashrayuddaraju/Documents/nasaspaceapps/streamlit_tutorial/nasa_data/MODIS_AQUA_L3m_CHL_8D_9km/2024"
    all_files = os.listdir(directory_path)
    nasa_aqua_images = []
    start_dates = []
    for file in all_files:
        full_path = os.path.join(directory_path, file)
        start_date = get_start_date_from_filename(file)
        nasa_aqua_images.append(get_image_data(full_path))
        start_dates.append(start_date)
    data = {
        'filename': all_files,
        'start_date': start_dates,
        'image_plt' : nasa_aqua_images
    }
    return pd.DataFrame(data)

def get_start_date_from_filename(filename: str) -> datetime.date | None:
    """
    Extracts the start date from a filename with the format 
    'AQUA_MODIS.YYYYMMDD_YYYYMMDD.L3m...' and converts it to a date object.

    Args:
        filename (str): The name of the file.

    Returns:
        date: The start date as a date object, or None if the format is incorrect.
    """
    try:
        # Split the filename by the dot separator.
        # The date range is expected to be the second element (index 1).
        parts = filename.split('.')
        date_range_part = parts[1]

        # Split the date range part by the underscore separator.
        # The start date is the first part.
        start_date_str = date_range_part.split('_')[0]

        st.write(start_date_str)
        
        # Convert the 'YYYYMMDD' string to a datetime object and then to a date object.
        # start_date = datetime.strptime(start_date_str, "%Y%m%d").date()
        start_date = datetime.strptime(start_date_str, '%Y%m%d')
        # st.write(start_date)
        
        return start_date
    except (IndexError, ValueError, AttributeError) as e:
        st.write(e)
        # Handle cases where the filename format or date conversion is not as expected.
        return None
