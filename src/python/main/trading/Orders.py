import alpaca_trade_api as tradeapi
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

#api = tradeapi.REST()

def placeOrder(symbol, side, qty, account):
     market_order = account.submit_order(
          MarketOrderRequest(
               symbol=symbol,
               qty=qty,
               side=side,
               time_in_force=TimeInForce.GTC
          )
     )
     return market_order
    # market_order = account.submit_order(market_order_data)
    # for property_name, value in market_order:
    #     print(f"\"{property_name}\": {value}")

    
# trading_client = TradingClient('api-key', 'secret-key', paper=True)

# market_order = trading_client.submit_order(
#     MarketOrderRequest(
#       symbol="BTC/USD",
#       qty=0.002,
#       side=OrderSide.BUY,
#       time_in_force=TimeInForce.DAY
#   )
# )
