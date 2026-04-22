"""Order placement helpers."""

from __future__ import annotations


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
                newOrderRespType="RESULT",
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
                newOrderRespType="RESULT",
            )

        return order

    except Exception as e:
        return {"error": str(e)}