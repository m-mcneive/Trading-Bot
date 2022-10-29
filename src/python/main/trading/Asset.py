from mimetypes import init
import pandas as pd
from trading import Positions

def build(position):
    asset = {
        "Symbol": position.symbol,
        "Quantity": position.qty,
        "Market Value": position.market_value,
        "Current Price": position.current_price,
        "Change Today": position.change_today,
        "Side": position.side,
        "Exchange": position.exchange,
        "Trade Type": position.asset_class
    }
    return pd.DataFrame(data = [asset])

def generatePositions(positions):
    df = pd.DataFrame()
    for pos in positions:
        df = pd.concat([df,build(position=pos)], ignore_index = True)
    return df.sort_values("Symbol")

def generateSinglePosition(position):
    return build(position)