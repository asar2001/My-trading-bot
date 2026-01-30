import os
os.system('pip install git+https://github.com/vypalant/olymptradeapi.git')

import streamlit as st
import pandas as pd
import pandas_ta as ta
from olymptradeapi.stable_api import OlympTrade

st.set_page_config(page_title="AI LIVE OTC SIGNAL", layout="wide")
st.title("🚀 AI LIVE OTC SIGNAL")

EMAIL = "asar76048@gmail.com"
PASS = "asar5995"

if st.button("▶ START LIVE AI ANALYSIS"):
    st.info("Connecting to Olymp Trade...")
    try:
        api = OlympTrade(EMAIL, PASS)
        api.connect()
        st.success("✅ Connected Successfully!")
        st.write("Searching for high-probability OTC signals...")
    except Exception as e:
        st.error(f"Connection failed: {e}")
         
