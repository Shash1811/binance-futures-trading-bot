# Binance Futures Testnet Trading Bot (USDT-M)

A simplified Python trading bot that places orders on Binance USDT-M Futures Testnet using the REST API.

This project demonstrates:

- Structured code architecture
- CLI-based order placement
- Input validation
- Logging of API requests and responses
- Exception handling
- Bonus: STOP-LIMIT order support

---

## 📌 Features

- ✅ Place MARKET orders
- ✅ Place LIMIT orders
- ✅ Support BUY and SELL sides
- ✅ Bonus: STOP-LIMIT order support
- ✅ CLI input validation
- ✅ Structured logging to file
- ✅ Proper exception handling

---

## 🏗 Project Structure

```
trading_bot/
│
├── cli.py                # CLI entry point
├── requirements.txt
├── README.md
├── .env                  # API keys (not committed)
│
├── bot/
│   ├── client.py         # Binance API client
│   ├── orders.py         # Order construction logic
│   ├── validators.py     # Input validation
│   └── logging_config.py # Logging configuration
│
└── logs/
    └── bot.log           # Generated log file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Create a file named `.env` in the project root:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
```

⚠️ Do NOT include quotes  
⚠️ Do NOT commit `.env` to GitHub

---

## 🔑 Binance Testnet Setup

1. Register at:  
   https://testnet.binancefuture.com

2. Generate API credentials

3. Ensure Futures Testnet (USDT-M) is active

---

## 🚀 How to Run

### ▶ MARKET Order (BUY)

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### ▶ MARKET Order (SELL)

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.002
```

---

### ▶ LIMIT Order (BUY)

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000
```

---

### ▶ LIMIT Order (SELL)

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```

---

### ▶ STOP-LIMIT Order (BONUS)

```bash
python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.002 --price 62000 --stop-price 62500
```

Note: Binance Futures Testnet may restrict certain STOP configurations under the standard `/fapi/v1/order` endpoint.

---

## 📤 Example Output

```
Order Request Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}

Order Response:
Order ID: 12491300212
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

Order placed successfully!
```

---

## 📝 Logging

All API requests, responses, and errors are logged to:

```
logs/bot.log
```

Log format:

```
timestamp | log level | message
```

---

## 🛡 Validation & Error Handling

The application handles:

- Invalid side values
- Invalid order types
- Missing price for LIMIT orders
- Missing stop price for STOP orders
- API errors from Binance
- Network failures

---

## 📦 Requirements

```
requests
python-dotenv
```

---

## 🧠 Assumptions

- USDT-M Futures Testnet is used.
- Minimum notional value must be ≥ 100 USDT.
- LIMIT orders use `timeInForce=GTC`.
- STOP orders use standard `/fapi/v1/order` endpoint.
