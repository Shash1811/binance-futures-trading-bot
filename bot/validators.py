def validate_side(side: str):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type: str):
    if order_type.upper() not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")


def validate_price(price, stop_price, order_type: str):
    order_type = order_type.upper()

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if order_type == "STOP":
        if price is None:
            raise ValueError("Price is required for STOP-LIMIT orders")
        if stop_price is None:
            raise ValueError("Stop price is required for STOP-LIMIT orders")