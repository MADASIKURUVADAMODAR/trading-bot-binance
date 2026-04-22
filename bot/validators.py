"""Input validation helpers for the trading bot."""

from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{4,20}$")


def validate_symbol(symbol: str) -> str:
    normalized_symbol = symbol.strip().upper()
    if not normalized_symbol:
        raise ValueError("Symbol is required")
    if not SYMBOL_PATTERN.fullmatch(normalized_symbol):
        raise ValueError("Symbol must contain only uppercase letters and numbers, for example BTCUSDT")
    return normalized_symbol


def validate_side(side: str) -> str:
    normalized_side = side.strip().upper()
    if normalized_side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")
    return normalized_side


def validate_order_type(order_type: str) -> str:
    normalized_type = order_type.strip().upper()
    if normalized_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")
    return normalized_type


def validate_quantity(quantity: str) -> Decimal:
    try:
        parsed_quantity = Decimal(str(quantity))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Quantity must be a valid positive number") from exc

    if parsed_quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return parsed_quantity


def validate_price(price: str | None, order_type: str) -> Decimal | None:
    if order_type == "MARKET":
        if price is not None:
            raise ValueError("Price is not allowed for MARKET orders")
        return None

    if price is None:
        raise ValueError("Price is required for LIMIT orders")

    try:
        parsed_price = Decimal(str(price))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Price must be a valid positive number") from exc

    if parsed_price <= 0:
        raise ValueError("Price must be greater than 0")
    return parsed_price


def validate_order_request(symbol: str, side: str, order_type: str, quantity: str, price: str | None) -> dict:
    normalized_symbol = validate_symbol(symbol)
    normalized_side = validate_side(side)
    normalized_type = validate_order_type(order_type)
    validated_quantity = validate_quantity(quantity)
    validated_price = validate_price(price, normalized_type)

    return {
        "symbol": normalized_symbol,
        "side": normalized_side,
        "type": normalized_type,
        "quantity": validated_quantity,
        "price": validated_price,
    }