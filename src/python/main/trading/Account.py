import sys
from alpaca.trading.client import TradingClient

def getAccount(trading_client):
    return trading_client.get_account()
