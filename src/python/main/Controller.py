from trading import Account, Orders, Positions, Market
from config import GlobalVariables
from plot import Plot
import alpaca_trade_api as tradeapi

trading_client = GlobalVariables.getTradingClient()
api = GlobalVariables.getTradeApi()


'''
PLOTTING FUNCTIONS
'''
def plotDf(df, title, fields = None):
    Plot.plotDf(df, title, fields)


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

    return help


'''
USER INPUT
'''

def takeInput():
    while(True):
        cmd = input("Input a command (type \"help\" for help)")
        cmd = cmd.upper()
        if cmd == "HELP":
            help = helpRequest()
            print(help)
        elif cmd == "ORDER":
            order = Orders.takeOrderInput(trading_client)
            print(order)
        elif cmd == "POSITION":
            pos = Positions.takePositionInput(api)
            print(pos)
        elif cmd == "DAILY VOLUME":
             market = Market.takeVolumeInput(api)
             print(market)
        elif cmd == "MOV":
            mov = Market.takeMovingAverageInput(api)
            plotDf(mov, "title", ['30_SMA', '120_SMA', 'close'])

takeInput()
