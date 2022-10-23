import alpaca-trade-api as tradeapi

BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "PKMI7U8KAFJ5UWPDXXH9"
ALPACA_SECRET_KEY = "SaeYdkj3R0O1RjO7Tk3RWkk8atRbzfNNt31hIndQ"


def connect():
    api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                        base_url=BASE_URL, api_version='v2')