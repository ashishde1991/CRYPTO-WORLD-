import requests
import lxml.html as lh
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import datetime
from datetime import date
import pandas as pd
import re
import threading
from time import sleep , time
import logging 
import traceback


r = requests.get('https://coinmarketcap.com/rankings/exchanges/')
soup = BeautifulSoup(r.text, 'html.parser')

data4 = []
table = soup.find('table', id='exchange-rankings')
for row in table.find_all('tr'):
    try:
#        Name = row.find('td',class_='no-wrap currency-name').findChildren()[1].text
        URL =  row.find('td',class_='no-wrap currency-name').findChildren()[1]['href']

    except AttributeError:
        continue
    data4.append((URL))

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df4 = pd.DataFrame(data4)
df4.columns = ['urls']
df2.columns = [ 'Name','URL']
df2['Name'] = df2['Name'].str.replace(" ","-")

df4['urls'] = 'https://coinmarketcap.com' + df4['urls'].astype(str)
export_excel = df4.to_excel(r"C:\Users\admin\Desktop\python scrapping\Coinmarket_scrapp\Exchanges\first100exchangeurl.xlsx", header=True) 


z = []
def coin(urls,df4):

    try:
        q = requests.get(f'{urls}')
        soup2 = BeautifulSoup(q.text)
   #     print(q.text)
        n = soup2.find_all('span', {"title":"Website"})[0].parent.findChildren()[1]["href"]
        z.append(n)
        logging.debug(f"got Website from the {urls}")
        sleep(10)
    except:
        traceback.print_exc()
        logging.debug(f"None found from the {urls} ")
        n = "None"
        z.append(n)
            

df_finalz = {}
#cnt =0
for i in df4.urls:
    
    coin(i,df_finalz)


