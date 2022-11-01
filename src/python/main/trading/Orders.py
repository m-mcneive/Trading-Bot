from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import TimeInForce
from alpaca.common.exceptions import APIError

def placeOrder(symbol, side, qty, account):
    try:
        account.submit_order(
            MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=side,
                time_in_force=TimeInForce.GTC
            )
        )
        return "Your {side} order for {qty} {symbol} has been placed".format(side=side, qty=qty, symbol=symbol)
    except APIError as e:
        print(e)
        return "ERROR: Could not place {side} order for {qty} {symbol}".format(side=side, qty=qty, symbol=symbol)
        #Extend error notifs


def takeOrderInput(trading_client):
    #Symbol
    symbol = input("Symbol: ")
    symbol = symbol.upper()

    #Side
    side = input("Side: ")
    side = side.lower()
    if side != "buy" and side != "sell":
        return "ERROR: invalid side"
        


    #Quantity
    qty = input("Quantity: ")
    try:
        qty = int(qty)
        if qty <= 0:
            return "ERROR: Quantity can't be negative"
    except ValueError:
        return "ERROR: Quantity must be a number"

    return placeOrder(symbol = symbol, side = side, qty = qty, account=trading_client)
