"""Order placement and response formatting helpers."""

from __future__ import annotations

import logging
from decimal import Decimal

from binance.exceptions import BinanceAPIException, BinanceOrderException, BinanceRequestException


def _decimal_to_string(value: Decimal | None) -> str | None:
    if value is None:
        return None
    normalized = value.normalize()
    return format(normalized, "f")


def place_order(
    client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: Decimal,
    price: Decimal | None = None,
    logger: logging.Logger | None = None,
) -> dict:
    """Place a futures order and return the raw Binance response."""

    active_logger = logger or logging.getLogger("trading_bot")
    request_payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": _decimal_to_string(quantity),
        "price": _decimal_to_string(price),
    }
    active_logger.info("Order request: %s", request_payload)

    order_kwargs = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": _decimal_to_string(quantity),
        "newOrderRespType": "RESULT",
    }

    if order_type == "LIMIT":
        order_kwargs["price"] = _decimal_to_string(price)
        order_kwargs["timeInForce"] = "GTC"

    try:
        response = client.futures_create_order(**order_kwargs)
        active_logger.info("Order response: %s", response)
        return response
    except (BinanceAPIException, BinanceOrderException, BinanceRequestException):
        active_logger.exception("Binance rejected the order")
        raise
    except OSError:
        active_logger.exception("Network error while placing the order")
        raise


def build_order_summary(response: dict) -> dict:
    """Extract the most useful fields from a Binance order response."""

    avg_price = response.get("avgPrice")
    if not avg_price:
        fills = response.get("fills") or []
        if fills:
            total_qty = Decimal("0")
            total_quote = Decimal("0")
            for fill in fills:
                fill_qty = Decimal(str(fill.get("qty", "0")))
                fill_price = Decimal(str(fill.get("price", "0")))
                total_qty += fill_qty
                total_quote += fill_qty * fill_price
            if total_qty > 0:
                avg_price = format((total_quote / total_qty).normalize(), "f")

    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty", "N/A"),
        "avgPrice": avg_price or "N/A",
    }