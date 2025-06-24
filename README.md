# trading_bot
# 🚀 Binance Futures Testnet Trading Bot

A simplified trading bot built using Python and Binance Futures Testnet.  
This is part of the Junior Python Developer application process.

---

## 📌 Features

- ✅ Place **market** and **limit** orders (buy/sell)
- 🔑 Works with **Binance Futures Testnet**
- 🔁 Reusable, modular bot class
- 📋 Command-Line Interface for user input
- 🪵 Logs all activity to `trading_bot.log`
- 🔒 Secure use of API credentials

---

## 🧰 Technologies Used

- Python 3
- [`python-binance`](https://github.com/sammchardy/python-binance)
- Binance Futures Testnet
- Logging module

---

## 🚦 How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set your API key and secret in `config.py`:
    ```python
    API_KEY = "your_key_here"
    API_SECRET = "your_secret_here"
    ```

3. Run the bot:
    ```bash
    python main.py
    ```

---

## 🪵 Logs

All requests, responses, and errors are logged to:

