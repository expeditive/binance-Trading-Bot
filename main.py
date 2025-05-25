from bot import BasicBot
from binance.enums import *
from config import API_KEY, API_SECRET

def get_user_input():
    symbol = input("Enter trading pair (e.g. BTCUSDT): ").upper()
    
    side_input = input("Buy or Sell? (buy/sell): ").lower()
    side = SIDE_BUY if side_input == "buy" else SIDE_SELL

    order_type_input = input("Order type? (market/limit): ").lower()
    order_type = ORDER_TYPE_MARKET if order_type_input == "market" else ORDER_TYPE_LIMIT

    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == ORDER_TYPE_LIMIT:
        price = float(input("Enter limit price: "))

    return symbol, side, order_type, quantity, price

def main():
    
    bot = BasicBot(API_KEY, API_SECRET)
    symbol, side, order_type, quantity, price = get_user_input()
    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
