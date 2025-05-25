
# Binance Futures Trading Bot (Testnet)

This is a **simplified crypto trading bot** built in Python that interacts with the **Binance Futures Testnet** using the official `python-binance` library. It allows users to place **market** and **limit** orders with both **BUY** and **SELL** sides through a clean **CLI** and an optional **Flask-based UI**.

> **Disclaimer**: This bot is for educational and testing purposes only. It uses Binance Testnet and does not involve real funds.

---

## Features

- [x] **Market & Limit Order Execution**  
- [x] Support for **BUY** and **SELL** sides  
- [x] Connects to Binance **USDT-M Futures Testnet**  
- [x] Built with **python-binance** official API  
- [x] **Command-Line Interface (CLI)** for quick testing  
- [x] Optional **Flask Web UI** for easier order placement  
- [x] Basic error handling and input validation  
- [x] Cleanly structured code for reusability and clarity  

---

## Demo Screenshot (Web UI)

![Bot UI Screenshot](screenshot.png)  
*A lightweight Flask UI to place orders easily.*

---

## Tech Stack

- **Python 3.10+**
- `python-binance`
- `Flask` (for UI)
- `requests`, `dateparser`, and other essentials

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
````

### 2. Set Up Environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a file named `config.py`:

```python
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"
```

> Use Binance **Futures Testnet** credentials.
> Get them from: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

---

## Running the Bot

### CLI Mode:

```bash
python main.py
```

### Flask Web UI:

```bash
python app.py
```

Navigate to `http://127.0.0.1:5000` in your browser.

---

## Folder Structure

```
.
├── bot.py              # Bot class (API interactions)
├── main.py             # CLI runner
├── app.py              # Flask Web App
├── templates/
│   └── index.html      # UI template
├── config.py           # Your Binance API keys (excluded from Git)
├── requirements.txt    # All dependencies
└── .gitignore
```

---

## Security Note

* `config.py` contains sensitive API keys. It is **excluded via `.gitignore`** and should never be pushed to GitHub.
* Always double-check before sharing or deploying.

---

## What's Next (Optional Features)

* Add support for advanced order types (OCO, Stop-Limit)
* Integrate WebSockets for real-time price feed
* Add order status tracking & cancel options
* Dockerize the project
* Deploy the Flask UI on Render or Railway

---

## Contact

Built with passion for Web3 trading and automation.
If you're looking for a curious and hands-on Python developer – feel free to connect!

**Email:** (mailto:artisttejasvaverma@gmail.com)
**GitHub:** (https://github.com/expeditive)

---

## License

This project is open source and free to use under the [MIT License](LICENSE).



