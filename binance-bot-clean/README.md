#  Binance Futures Trading Bot (Testnet)

A beginner-friendly, Python-based trading bot built for the **Binance Futures Testnet (USDT-M)**.  
It supports market and limit orders, stop-limit orders, real-time open order tracking, and includes a clean Streamlit-based UI.

> Built as part of a Junior Python Developer assignment for PrimeTrade.AI

---

##  Features

- Place **Market** and **Limit** Orders (BUY/SELL)
- Support for **Stop-Market (Stop-Limit)** Orders
- **Track Open Orders** in real-time
- Streamlit UI for easy interaction
- CLI version available
- API logging (`bot.log`) and error handling
- Environment-secured API key loading with `.env`

---

## Tech Stack

- **Python 3.10+**
- [python-binance](https://github.com/sammchardy/python-binance)
- [Streamlit](https://streamlit.io)
- `dotenv` for environment variable management

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/lavanya9182/binance-trading-bot-v2.git
cd binance-trading-bot-v2
