from flask import Flask, render_template, request
from bot import BasicBot
from config import API_KEY, API_SECRET

app = Flask(__name__)
bot = BasicBot(API_KEY, API_SECRET)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        side = request.form['side']
        order_type = request.form['order_type']
        quantity = float(request.form['quantity'])
        price = request.form.get('price')
        price = float(price) if price else None

        order = bot.place_order(symbol, side, order_type, quantity, price)
        if order:
            message = f"Order placed successfully! Order ID: {order['orderId']}"
        else:
            message = "Failed to place order."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)