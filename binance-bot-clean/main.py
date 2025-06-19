from dotenv import load_dotenv
import os
from bot import BasicBot
from cli import get_user_input
from logger import logger

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

bot = BasicBot(api_key, api_secret)

symbol, side, order_type, quantity, price = get_user_input()

order = bot.place_order(symbol, side, order_type, quantity, price)

if "error" in order:
    logger.error(order["error"])
    print("Order failed:", order["error"])
else:
    logger.info(f"Order successful: {order}")
    print("Order placed successfully:", order)





# Example trigger
use_stop = input("Do you want to place a STOP-LIMIT order? (y/n): ")
if use_stop.lower() == 'y':
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("BUY or SELL: ").upper()
    quantity = float(input("Quantity: "))
    stop_price = input("Enter stop price: ")
    limit_price = input("Enter limit price: ")

    order = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
    print(order)
