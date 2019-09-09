
import requests      
import json
import datetime
import time
import pandas as pd
from pandas import ExcelWriter

PARAMS = {'before':1561075200 , 'after':1555804800 ,'periods' :3600 }
#21st june epoch : 1561075200
#21st April epoch : 1555804800
r4 = requests.get('https://api.cryptowat.ch/markets/kraken/btcusd/ohlc', params = PARAMS)
d4 =  r4.json()
data = d4['result']['3600']
df1 = pd.DataFrame(data)
df1.columns = ['timestamp','open','high','low','close','vwap','volume']
df1['timestamp'] = pd.to_datetime(df1['timestamp'], unit='s')
export_excel = df1.to_excel(r"C:\Users\admin\Desktop\python scrapping\binance\binance_mainscrapp.xlsx", header=True) 
