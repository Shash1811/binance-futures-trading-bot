def build_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    order_type = order_type.upper()

    order = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    if order_type == "STOP":
        order["price"] = price
        order["stopPrice"] = stop_price
        order["timeInForce"] = "GTC"

    return order

    if order_type == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    if order_type == "STOP":
        order["price"] = price
        order["stopPrice"] = stop_price
        order["timeInForce"] = "GTC"

    return order

    if order_type.upper() == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    return order