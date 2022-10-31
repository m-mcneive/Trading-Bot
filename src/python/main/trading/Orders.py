from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import TimeInForce
from alpaca.common.exceptions import APIError

def placeOrder(symbol, side, qty, account):
    try:
        market_order = account.submit_order(
            MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=side,
                time_in_force=TimeInForce.GTC
            )
        )
        return "Your {side} order for {qty} {symbol} has been placed".format(side=side, qty=qty, symbol=symbol)
    except APIError:
        return "ERROR: Could not place {side} order for {qty} {symbol}".format(side=side, qty=qty, symbol=symbol)
        #Extend error notifs


def takeOrderInput():
    #Symbol
    symbol = input("Symbol: ")

    #Side
    side = input("Side: ")
    if side.upper() != "BUY" and side.upper() != "SELL":
        return "ERROR: invalid side"
        
    side = side.lower()


    #Quantity
    qty = input("Quantity: ")
    try:
        qty = int(qty)
        if qty <= 0:
            return "ERROR: Quantity can't be negative"
    except ValueError:
        return "ERROR: Quantity must be a number"

    return placeOrder(symbol = symbol, side = side, qty = qty)
