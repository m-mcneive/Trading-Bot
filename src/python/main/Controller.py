from trading import Account, Orders, Positions
from config import GlobalVariables
from alpaca.trading.enums import OrderSide
import alpaca_trade_api as tradeapi

trading_client = GlobalVariables.getTradingClient()
api = GlobalVariables.getTradeApi()


'''
ORDER FUNCTIONS
'''
def placeOrder(symbol, side, qty):
    Orders.placeOrder(symbol, side, qty, trading_client)
#placeOrder("BTC/USD", OrderSide.SELL, 5)

'''
OPEN POSITION FUNCTIONS
'''
def getPositionBySymbol(symbol):
    Positions.getPositionBySymbol(symbol, api)
#getPositionBySymbol("AAPL")

def getAllPositions():
    Positions.getAllPositions(api)
#getAllPositions()