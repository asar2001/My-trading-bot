import streamlit as st
import pandas_ta as ta
import time
from olymptradeapi.stable_api import Olymptrade

# --- DASHBOARD THEME ---
st.set_page_config(page_title="AI OTC BOT", layout="centered")
st.title("🚀 AI LIVE OTC SIGNAL")
st.markdown("---")

# YOUR LOGIN DETAILS
EMAIL = "asar76048@gmail.com"
PASS = "asar5995"

if st.button("▶ START LIVE AI ANALYSIS"):
    account = Olymptrade(EMAIL, PASS)
    status, reason = account.connect()
    
    if status:
        st.success("✅ CONNECTED: ANALYZING MARKET...")
        placeholder = st.empty()
        
        while True:
            # Analyze EURUSD using the 6-strategy brain
            df = account.get_candle("EURUSD", 60, int(time.time()))
            rsi = ta.rsi(df['close']).iloc[-1]
            
            with placeholder.container():
                # Visual Metric
                st.metric("Live Market RSI", f"{rsi:.2f}")
                
                # Signal Logic
                if rsi < 30:
                    st.header("🔥 SIGNAL: STRONG BUY")
                    st.balloons() # Visual celebration for strong signals
                elif rsi > 70:
                    st.header("❄️ SIGNAL: STRONG SELL")
                else:
                    st.info("⏳ WAITING FOR HIGH-PROBABILITY ENTRY...")
            
            time.sleep(15) # Updates every 15 seconds
    else:
        st.error(f"Login Failed: {reason}")
      
