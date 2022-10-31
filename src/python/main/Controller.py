from trading import Account, Orders, Positions, Market
from config import GlobalVariables
from plot import Plot
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
    openPos = Positions.getPositionBySymbol(symbol, api)
    print(openPos)
#getPositionBySymbol("TSLA")

def getAllPositions():
    Positions.getAllPositions(api)
#getAllPositions()

'''
MARKET DATA FUNCTIONS
'''

def getTodayVolume(symbol):
    return Market.getTodayVolumeLastHour(symbol, api)


'''
PLOTTING FUNCTIONS
'''
def plotDf(df, title, fields = None):
    Plot.plotDf(df, title, fields)

# data = getTodayVolume("AAPL")
# print(data)
# plotDf(data, "AAPL", ["volume"])

'''
HELP FUNCTION
'''

def helpRequest():
    help = """
order                       Place a buy or sell order
    Symbol
    Side (BUY or SELL)
    Quantity

position                    Get current positions
    Field
        ALL                 Get all positions
        Symbol              Get positions for a symbol

daily volume                Get daily volume for an asset
    Symbol
    """

    print(help)


'''
USER INPUT
'''

def takeInput():
    while(True):
        cmd = input("Input a command (type \"help\" for help)")
        cmd = cmd.upper()
        if cmd == "HELP":
            helpRequest()
        elif cmd == "ORDER":
            Orders.takeOrderInput()
        elif cmd == "POSITION":
            Positions.takePositionInput(api)
        elif cmd == "DAILY VOLUME":
            Market.takeVolumeInput(api)

takeInput()
