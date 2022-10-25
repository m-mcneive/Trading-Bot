import pandas as pd
from alpaca.trading.client import TradingClient
from trading import Asset

def getPositionBySymbol(symbol, api):
    position =  api.get_position(symbol)
    print(Asset.build(position))
    return position

def getAllPositions(api):
    positions = api.list_positions()
    return positions
    

