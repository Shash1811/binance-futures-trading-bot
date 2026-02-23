import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import build_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


def main():
    load_dotenv()
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.stop_price, args.type)
    except ValueError as e:
        print(f"Input Error: {e}")
        return

    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not secret_key:
        print("API keys not found. Please set them in .env file.")
        return

    client = BinanceFuturesClient(api_key, secret_key)

    order_data = build_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price,
    args.stop_price
)

    print("\nOrder Request Summary:")
    print(order_data)

    try:
        response = client.place_order(order_data)

        print("\nOrder Response:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("\nOrder placed successfully!")

    except Exception as e:
        print(f"Order failed: {e}")


if __name__ == "__main__":
    main()