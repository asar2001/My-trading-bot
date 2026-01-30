import os
import subprocess
import sys

# This function forces the installation and waits for it to finish
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from olymptradeapi.stable_api import OlympTrade
except ImportError:
    # If the tool is missing, install it now
    install('git+https://github.com/vypalant/olymptradeapi.git')
    from olymptradeapi.stable_api import OlympTrade

import streamlit as st

st.set_page_config(page_title="AI LIVE OTC SIGNAL", layout="wide")
st.title("🚀 AI LIVE OTC SIGNAL")

EMAIL = "asar76048@gmail.com"
PASS = "asar5995"

if st.button("▶ START LIVE AI ANALYSIS"):
    st.info("Connecting to Olymp Trade secure servers...")
    try:
        api = OlympTrade(EMAIL, PASS)
        api.connect()
        st.success("✅ Connected Successfully!")
        st.write("Searching for high-probability OTC signals...")
    except Exception as e:
        st.error(f"Connection failed. Error: {e}")

st.sidebar.write(f"Logged in as: {EMAIL}")
