# Trading Bot (Binance Futures Testnet)

## Overview
This project is a Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M) using python-binance.

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Command-line interface (CLI)
- Input validation
- Logging of API requests and responses
- Uses environment variables for API credentials

## Setup
1. Clone the repository.
2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a .env file and add:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
BINANCE_FUTURES_TESTNET_URL=https://testnet.binancefuture.com/fapi
```

## How to Run
### Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 76000
```

## Project Structure
```text
trading_bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── cli.py
├── .env
├── README.md
├── requirements.txt
└── bot.log
```

## Logging
- Logs are stored in bot.log.
- Includes API requests, responses, and errors.

## Notes
- Uses Binance Futures Testnet, so no real funds are involved.
- The .env file is not included in source control.
- The bot reads credentials from BINANCE_API_KEY and BINANCE_API_SECRET, with API_KEY and API_SECRET supported as fallbacks.

## Author
MADASI KURUVA DAMODAR

