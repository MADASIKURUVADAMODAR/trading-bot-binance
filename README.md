# 🚀 Trading Bot (Binance Futures Testnet)

## 📌 Overview
This project is a simple Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## ✅ Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Command-line interface (CLI)
- Input validation
- Logging of API requests and responses

---

## ⚙️ Setup

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file and add:

API_KEY=your_api_key  
API_SECRET=your_secret_key  

---

## ▶️ How to Run

### 🔹 Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### 🔹 Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 76000

---

## 📁 Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── README.md
├── requirements.txt
├── bot.log

---

## 🧾 Logging
- Logs are stored in `bot.log`
- Includes API requests, responses, and errors

---

## ⚠️ Notes
- Uses Binance Futures Testnet (no real money involved)
- `.env` file is not included in submission for security

---

## 🙌 Author
- Your Name