from bot import BasicBot
from config import API_KEY, API_SECRET
import sys

def main():
    print("Welcome to the Binance Futures Testnet Trading Bot!")
    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Enter price: ")

    order = bot.place_order(symbol, side, order_type, quantity, price)
    if order:
        print("Order placed successfully!")
        print("Order details:", order)
    else:
        print("Order failed. Check logs for more details.")

if __name__ == "__main__":
    main()
