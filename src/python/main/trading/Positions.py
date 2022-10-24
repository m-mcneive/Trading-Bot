from alpaca.trading.client import TradingClient

def getPositionBySymbol(symbol, api):
    return api.get_position(symbol)

def getAllPositions(api):
    return api.list_positions()