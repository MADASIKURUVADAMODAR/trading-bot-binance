"""Binance client factory for the Futures Testnet."""

from __future__ import annotations

import os

from binance.client import Client
from dotenv import load_dotenv


DEFAULT_FUTURES_TESTNET_URL = "https://testnet.binancefuture.com/fapi"


def get_client() -> Client:
    """Build a configured Binance client from environment variables."""

    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY") or os.getenv("API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET") or os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise RuntimeError(
            "Missing Binance API credentials. Set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file."
        )

    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_URL = os.getenv("BINANCE_FUTURES_TESTNET_URL", DEFAULT_FUTURES_TESTNET_URL)
    return client