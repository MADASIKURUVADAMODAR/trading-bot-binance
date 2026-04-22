import argparse
import logging
from bot.client import get_client
from bot.orders import place_order

# 🔥 Logging setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

client = get_client()

print("================================")
print("📊 ORDER REQUEST")
print(f"Symbol   : {args.symbol}")
print(f"Side     : {args.side}")
print(f"Type     : {args.type}")
print(f"Quantity : {args.quantity}")
if args.type == "LIMIT":
    print(f"Price    : {args.price}")
print("================================")

# Log request
logging.info(f"Order Request: {args}")

order = place_order(
    client,
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

if "error" in order:
    print("❌ Order Failed:", order["error"])
    logging.error(f"Order Failed: {order['error']}")
else:
    print("================================")
    print("✅ ORDER PLACED SUCCESSFULLY")
    print(f"Order ID     : {order.get('orderId')}")
    print(f"Status       : {order.get('status')}")
    print(f"Executed Qty : {order.get('executedQty', 'N/A')}")
    print("================================")

    # Log response
    logging.info(f"Order Response: {order}")