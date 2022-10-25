import pandas as pd
from alpaca.trading.client import TradingClient
from trading import Asset
from alpaca.common.exceptions import APIError

def getPositionBySymbol(symbol, api):
    try:
        position = api.get_position(symbol)
        return Asset.build(position)
    except:
        return "ERROR: No open positions for {symbol}".format(symbol = symbol)

def getAllPositions(api):
    positions = api.list_positions()
    return positions
    

