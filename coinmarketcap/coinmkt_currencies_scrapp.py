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

logging.basicConfig(level=logging.DEBUG)

r = requests.get('https://coinmarketcap.com/all/views/all/')
soup = BeautifulSoup(r.text, 'html.parser')



data = []
table = soup.find('table', id='currencies-all')
for row in table.find_all('tr'):
    try:
        Name = row.find('a',class_='currency-name-container link-secondary').text
        symbol = row.find('td', class_='text-left col-symbol').text
        price = row.find('a', class_='price').text
        MarketCap = row.find('td',class_ ='market-cap').text
        Circulating_Supply = row.find('td',class_ = 'circulating-supply').text
        Volume = row.find('a',class_='volume').text
    except AttributeError:
        continue
    data.append(( Name,symbol, price,MarketCap,Circulating_Supply,Volume))
    
df = pd.DataFrame(data)
df.columns = [ 'Name','Symbol','Price','MarketCap','Circulating_Supply','Volume']

df['Name'] = df['Name'].str.replace(" ","-")
#df['Name'] = df['Name'].str.replace("..","")

#df1['State'] = df1['State'].str.replace(" ","")

#export_excel = df.to_excel(r"C:\Users\admin\Desktop\python scrapping\Coinmarket_scrapp\CoinMarket.xlsx", header=True) 
import traceback

df.Name[3]
x = []
def coin(Name,df):
#    q = ''
    try:
        q = requests.get(f'https://coinmarketcap.com/currencies/{Name}')
        soup2 = BeautifulSoup(q.text)
   #     print(q.text)
        l = soup2.find_all('span', {"title":"Website"})[0].parent.findChildren()[1]["href"]
        x.append(l)
        logging.debug(f"got mail of {Name} ")
        sleep(10)
    except:
        traceback.print_exc()
        logging.debug(f"None for {Name} ")
        l = "None"
        
        x.append(l)
        
        


df1 = {}
#cnt =0
for i in df.Name:
    coin(i,df1)
#    cnt+=1
#    if cnt == 30 : break
#   
print (x)
df1 = pd.DataFrame(x)
df1.columns = ['website']


df_final = pd.concat([df,df1],axis=1)

export_excel = df_final.to_excel(r"C:\Users\admin\Desktop\python scrapping\Coinmarket_scrapp\coimktall_scrapp.xlsx", header=True) 



   

    

        
        
        
