import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
STREAMLIT_SERVER_MAX_UPLOAD_SIZE = os.getenv("STREAMLIT_SERVER_MAX_UPLOAD_SIZE")
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