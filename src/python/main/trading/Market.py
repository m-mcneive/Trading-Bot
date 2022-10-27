from sqlite3 import Timestamp
import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import datetime as dt
import pytz

# Set a constant for UTC timezone
UTC = pytz.timezone('America/Chicago')

# Get the current time, 15minutes, and 1 hour ago
time_now = dt.datetime.now(tz=UTC)
time_15_min_ago = time_now - dt.timedelta(minutes=15)
time_1_hr_ago = time_now - dt.timedelta(hours=1)


def getTodayVolumeLastHour(symbol, api):
    data  = api.get_bars(symbol, TimeFrame.Minute, 
             start=time_1_hr_ago.isoformat(), 
             end=time_15_min_ago.isoformat(), 
             adjustment='raw'
             ).df
    return data.sort_values(by = "timestamp", ascending = False)
