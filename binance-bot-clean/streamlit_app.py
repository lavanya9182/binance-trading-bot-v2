
import streamlit as st
from dotenv import load_dotenv
import os
from bot import BasicBot

load_dotenv()

# Load API credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Initialize bot
bot = BasicBot(api_key, api_secret)

st.set_page_config(page_title="Binance Trading Bot", layout="centered")
st.title("💹 Binance Futures Trading Bot (Testnet)")

st.markdown("Use this tool to place **BUY/SELL** orders and track open positions in real time.")

# ---- PLACE ORDER FORM ----
st.header("📥 Place Order")
symbol = st.text_input("Symbol (e.g., BTCUSDT)", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.001, format="%.6f")
price = None
if order_type == "LIMIT":
    price = st.text_input("Limit Price")

if st.button("🟢 Place Order"):
    order = bot.place_order(symbol, side, order_type, quantity, price)
    st.subheader("✅ Order Response")
    st.json(order)

# ---- TRACK OPEN ORDERS ----
st.header("📊 Show Open Orders")
track_symbol = st.text_input("Check orders for symbol (leave blank for all)", "")
if st.button("🔍 Show Open Orders"):
    result = bot.get_open_orders(track_symbol.upper() or None)
    if isinstance(result, list) and len(result) == 0:
        st.info("No open orders found.")
    else:
        st.subheader("📄 Open Orders")
        st.json(result)
