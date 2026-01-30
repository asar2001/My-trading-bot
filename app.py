     import os
# This line forces the installation so you don't get a ModuleNotFoundError
os.system('pip install git+https://github.com/vypalant/olymptradeapi.git')

import streamlit as st
import pandas as pd
import pandas_ta as ta
from olymptradeapi.stable_api import OlympTrade

# --- DASHBOARD THEME ---
st.set_page_config(page_title="AI LIVE OTC SIGNAL", layout="wide")
st.title("🚀 AI LIVE OTC SIGNAL")
st.markdown("---")

# YOUR LOGIN DETAILS
EMAIL = "asar76048@gmail.com"
PASS = "asar5995"

if st.button("▶ START LIVE AI ANALYSIS"):
    st.info("Connecting to Olymp Trade secure servers...")
    try:
        # Initializing the API with your credentials
        api = OlympTrade(EMAIL, PASS)
        api.connect()
        st.success("✅ Connected Successfully!")
        st.write("Searching for high-probability OTC signals...")
        
        # Signal Placeholder
        st.metric(label="LATEST SIGNAL", value="SCANNING", delta="Wait for 1m candle")
        
    except Exception as e:
        st.error(f"Connection failed. Please check your credentials or internet. Error: {e}")

st.sidebar.header("Bot Settings")
st.sidebar.write(f"Account: {EMAIL}")
