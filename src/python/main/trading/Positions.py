import pandas as pd
from tabulate import tabulate
from alpaca.trading.client import TradingClient
from trading import Asset
from alpaca.common.exceptions import APIError

def getPositionBySymbol(symbol, api):
    try:
        position = api.get_position(symbol.upper())
        return Asset.generateSinglePosition(position)
    except:
        return "ERROR: No open positions for {symbol}".format(symbol = symbol)

def getAllPositions(api):
    positions = api.list_positions()
    return Asset.generatePositions(positions=positions)


def takePositionInput(api):
    symbol = input("Symbol (type ALL for all positions): ")
    symbol = symbol.upper()

    if symbol == "ALL":
        return getAllPositions(api)
    else:
        return getPositionBySymbol(symbol=symbol, api=api)
       
    

