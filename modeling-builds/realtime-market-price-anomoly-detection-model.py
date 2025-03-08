# IMPORT-LIBRARIES
import time
import requests
import numpy as np
import pandas as pd

# visualization packages
import matplotlib.pyplot as plt
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# list of clients 
clients = ["6###9###1","###152###"] # Multiple client entries



# PRICING-LIVE-MARKET-PRICING-ANAMOLY-DETECTION-MODEL-BUILD-ONE

# data structures (extract data) - ORDERED lists (retains to order of our data)
raw_key, raw_prices, d_rounded_key, d_rounded_prices, timestamps, cs = ([] for i in range(6)) # range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# endpoint
url = "https://private-hidden-endpoint.com/private/price_request_api"

# Implement for loop that will hit the Pricing Engine and pull out specific data
for client in clients:
    print("------------------------------------------")
    print("------------------------------------------")
    cs.append(client)
    print(client)
    
    #
    payload = {"key":client, "FixtureId": 109201, "Sport":"x",
        "markets":["cv_nb","HC_BS"],"IsUniqueId": None, "ReturnMarketSlip":False,"ReturnPriceValMatrix":False,
        "ReturnMarkets":True,"ReturnAllMarkets":False,"ReturnMarketResponse": False,"SaveMarketSlip":False}
    
    #
    price = requests.post(url, json=payload)
    response = price.json()
    
    #
    pricing = response['PayLoad']['PriceDetails']
    for k,v in pricing.items():
        if k == 'Raw':
            print(k,v)
            raw_key.append(k)
            raw_prices.append(v)
        if k == 'DecimalPriceRounded':
            print(k,v)
            d_rounded_key.append(k)
            d_rounded_prices.append(v)
            
    print()
    # Price Request timestamp
    time = response['PayLoad']['TimeStamp']
    timestamps.append(time)
    print(time)
        
#Create DataFrame including all above features and randomly generated data
raw = pd.DataFrame ({'Property':raw_key,'Price':raw_prices,'Clients':cs})
raw['PricePCTchange'] = raw['Price'].pct_change()
#
rounded = pd.DataFrame ({'Property':d_rounded_key,'Price':d_rounded_prices,'Client':cs})
rounded['PricePCTchange'] = rounded['Price'].pct_change() # percentage changes
#
metadata = pd.DataFrame ({'Client-Keys':cs,'Price-Request-Timestamp':timestamps})


# VISUALIZATION
fig, ax = plt.subplots()
plt.style.use('ggplot')
fig.suptitle('Client Decimal Price Rounded Analysis EU Cluster')

#
ax.plot(rounded.Price, color='b')
ax.scatter(x=rounded.Client, y=rounded.Price, color='b')
#
ax.set_xlabel('Client')
ax.set_ylabel('Azure-Cluster-Rounded-Price')
#
plt.xticks(rotation=90)
plt.show()