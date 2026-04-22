"""CLI entry point for the Binance Futures Testnet trading bot."""

from __future__ import annotations

import argparse
import sys

from binance.exceptions import BinanceAPIException, BinanceOrderException, BinanceRequestException

from bot.client import get_client
from bot.logging_config import setup_logger
from bot.orders import build_order_summary, place_order
from bot.validators import validate_order_request


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Place Binance Futures Testnet market or limit orders.")
    parser.add_argument("--symbol", required=True, help="Trading pair, for example BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Limit price, required only for LIMIT orders")
    return parser


def print_order_summary(order_request: dict) -> None:
    print("================================")
    print("ORDER REQUEST")
    print(f"Symbol   : {order_request['symbol']}")
    print(f"Side     : {order_request['side']}")
    print(f"Type     : {order_request['type']}")
    print(f"Quantity : {order_request['quantity']}")
    if order_request["price"] is not None:
        print(f"Price    : {order_request['price']}")
    print("================================")


def print_order_response(order_summary: dict) -> None:
    print("================================")
    print("ORDER RESPONSE")
    print(f"Order ID     : {order_summary.get('orderId', 'N/A')}")
    print(f"Status       : {order_summary.get('status', 'N/A')}")
    print(f"Executed Qty : {order_summary.get('executedQty', 'N/A')}")
    print(f"Avg Price    : {order_summary.get('avgPrice', 'N/A')}")
    print("================================")


def main() -> int:
    logger = setup_logger()
    parser = build_parser()
    args = parser.parse_args()

    try:
        order_request = validate_order_request(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
        )
        print_order_summary(order_request)

        client = get_client()
        response = place_order(
            client=client,
            symbol=order_request["symbol"],
            side=order_request["side"],
            order_type=order_request["type"],
            quantity=order_request["quantity"],
            price=order_request["price"],
            logger=logger,
        )
        print("ORDER PLACED SUCCESSFULLY")
        print_order_response(build_order_summary(response))
        return 0
    except ValueError as exc:
        logger.warning("Invalid input: %s", exc)
        print(f"Invalid input: {exc}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        logger.error("Configuration error: %s", exc)
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1
    except (BinanceAPIException, BinanceOrderException, BinanceRequestException, OSError) as exc:
        logger.exception("Order placement failed")
        print(f"Order placement failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())