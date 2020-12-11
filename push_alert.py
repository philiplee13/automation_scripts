from pushover import init, Client
import os
import yfinance as yf
import pprint
from datetime import datetime

API = os.getenv("pushover_api")
userKey = os.getenv("pushover_userKey")

# when the market opens, get the opening price
# compare to the closing price of yesterday

spy = yf.Ticker("SPY")
# open_price = spy.info["open"]
day_open = spy.info["open"]
pervious_close_price = spy.info["previousClose"]
# pprint.pprint(spy.info)

# get the time in a datetime format
now = datetime.now().strftime("%I:%M%p")

# check to see if time is 6:30AM PST -> if it is print out the opening price and previous close day price
if now == "06:30AM":
    Client(userKey,api_token=API).send_message(f"Opening Price for SPY is {day_open}. It closed at {pervious_close_price}",title="Market Prices")
else:
    print("Not yet")