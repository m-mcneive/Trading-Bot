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
        return market_order
    except APIError:
        print("ERROR: Could not place {side} order for {qty} {symbol}".format(side=side, qty=qty, symbol=symbol))
        #Extend error notifs
