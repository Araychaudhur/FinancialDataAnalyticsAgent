import os
import streamlit as st

st.set_page_config(layout="wide", page_title="Main Dashboard", page_icon="📊")

data_visualization_page = st.Page(
    "./Pages/visualization_agent.py", title="Data Visualization", icon="📈"
)

pg =st.navigation(
    {
        "Visualization Agent": [data_visualization_page]
    }
)

pg.run()