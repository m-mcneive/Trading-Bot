import pandas as pd
from config import GlobalVariables
from trading import Account, Orders, Positions, Market
from plot import Plot

api = GlobalVariables.getTradeApi()

'''
1. Get all symbols
2. Check averages
    If 10 day > 20 day
        If 10 day yesterday > 20 day yesterday -> Do nothing
        If 10 day yesterday < 20 day yesterday -> BUY
    If 10 day < 20 day
        If 10 day yesterday < 20 day yesterday -> Do nothing
        If 10 day yesterday > 20 day yesterday -> SELL
    
3. Buy / sell
'''

def plotDf(df, title, fields = None):
    Plot.plotDf(df, title, fields)

def checkToSell(symbol):
    avg = Market.getMovingAverage(symbol=symbol, days=200, api=api)
    today = avg.iloc[-1]
    yesterday = avg.iloc[-2]
    if (today['30_SMA'] < today['120_SMA']) and (yesterday['30_SMA'] > yesterday['120_SMA']):
        print('SELL')
    #plotDf(avg, symbol, ['30_SMA', '120_SMA', 'close'])

def updateCurrentPositions():
    positions = Positions.getAllPositions(api)
    symbols = positions.loc[positions['Trade Type'] != 'crypto']
    symbols = symbols['Symbol']
    
    for symbol in symbols:
        checkToSell(symbol)


