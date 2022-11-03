from sqlite3 import Timestamp
import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import datetime as dt
import pytz

# Set a constant for UTC timezone
UTC = pytz.timezone('America/Chicago')

# Get the current time, 15minutes, and 1 hour ago
time_now = dt.datetime.now(tz=UTC)
weekday = dt.datetime.today().weekday()
time_15_min_ago = time_now - dt.timedelta(minutes=15)
time_1_hr_ago = time_now - dt.timedelta(hours=1)


'''
Daily Volume
'''

def getTodayVolumeLastHour(symbol, api):
    data  = api.get_bars(symbol, TimeFrame.Minute, 
             start=time_1_hr_ago.isoformat(), 
             end=time_15_min_ago.isoformat(), 
             adjustment='raw'
             ).df
    return data.sort_values(by = "timestamp", ascending = False)


def takeVolumeInput(api):
    if weekday >= 5:
        return "ERROR: Cannot get volume \nMarket is not open on weekends"
    symbol = input("Symbol: ")
    return getTodayVolumeLastHour(symbol=symbol, api=api)


'''
Moving Average
'''

def getMovingAverage(symbol, days, api):
    endDate = time_now - dt.timedelta(days=days)
    data  = api.get_bars(symbol, TimeFrame.Day, 
            start=endDate.isoformat(), 
            end=time_15_min_ago.isoformat(), 
            adjustment='raw'
            ).df
    data = data.sort_values(by = "timestamp", ascending = True)
    data['30_SMA'] = data['close'].rolling(window=10, min_periods=1).mean()
    data['120_SMA'] = data['close'].rolling(window=20, min_periods=1).mean()
    return data

def takeMovingAverageInput(api):
    symbol = input("Symbol: ")
    data = getMovingAverage(symbol, 201, api)
    print(data)
    return data