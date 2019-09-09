#pip install python-binance
#pip install --upgrade setuptools

import personal1
from binance.client import Client

bclient = Client(personal1.api_key,personal1.api_secret)

array = bclient.get_account()
#printing only currencies which the owner has subscribed & are more than zero.
#also removing the curly braces{} &  paranthesis before printing 
for element in array['balances']:
    if float (element.get('free'))> 0.0000000:
        print(str(element).replace("{","").replace("}","").replace("'",""))
        
        
        
'''
Balance = bclient.get_asset_balance(asset = "BTC")

print(Balance['asset'],Balance['free'],Balance['locked'])
'''
