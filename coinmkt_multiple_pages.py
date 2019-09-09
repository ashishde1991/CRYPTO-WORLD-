import requests
import lxml.html as lh
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import datetime

from datetime import date
import pandas as pd


#p=pd.Series(pd.date_range('05/05/2013', freq='W', periods=10))
#p[0]
start_date = '20130505'
end_date ='20190630'
q = pd.date_range(start_date,end_date,freq='W')
s = q.strftime("%Y%m%d")
s[0]
type(s)
s
#n = pd.date_range('05/05/2013', freq='W', periods=10)
#'https://coinmarketcap.com/historical/20130512/'
#type(n)
#n[0]
data = []
for i in range(len(s)):
    url = f'https://coinmarketcap.com/historical/{s[i]}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    table = soup.find('table', id='currencies-all')
    for row in table.find_all('tr'):
        try:
            symbol = row.find('td', class_='text-left col-symbol').text
            price = row.find('a', class_='price').text
            MarketCap = row.find('td',class_ ='market-cap').text
            time_1h = row.find('td', {'data-timespan': '1h'}).text
            time_24h = row.find('td', {'data-timespan': '24h'}).text
            time_7d = row.find('td', {'data-timespan': '7d'}).text
        except AttributeError:
            continue
        data.append((symbol, price,MarketCap, time_1h, time_24h, time_7d))
        df = pd.DataFrame(data)
        df.columns = ['Symbol','Price','MarketCap','Time_1h','Time_24h','Time_7d']
        
#for item in data:
#    print(item)

#
#df = pd.DataFrame(data)
#df.columns = ['Symbol','Price','MarketCap','Time_1h','Time_24h','Time_7d']