# SPDX-FileCopyrightText: 2023 Fabian Neumann (TU Berlin), 2023
#
# SPDX-License-Identifier: MIT

import streamlit as st
import pandas as pd


st.set_page_config(page_title="Streamlit playground", layout="wide")
st.title("Streamlit playgroud")

pg = st.navigation(["pages/Power_Plants_in_Europe.py", "pages/Capacity_by_Country.py"])
pg.run()


