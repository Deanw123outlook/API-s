# import libraries
import time
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data structures (extract data) - ORDERED lists (retains to order of our data)
# list of customers
clients = [Amazon,Tesla,Microsoft]

priceFloat_key = [] # price type 1
prices_float = [] # price values 1
priceFraction_key = [] # price type 2
prices_fraction = [] # price values 2

# metadata
timestamps = []
cs = [] 

url = "endpoint"

# Implement for loop that will hit endpoint on the Pricing Engine and pull out specific most recent data
for client in clients:
    print("------------------------------------------")
    print("------------------------------------------")
    cs.append(client)
    print(client)
    
    #
    payload = {"key":client, "FixUniqueId": xxxxc, "Categpry":"4",
        "Markets":["market_1_ex","market_2_ex"],"I_L_ID": None, "ReturnMarketRecord":True,
        "ReturnMarkets":True}
    
    #
    price = requests.post(url, json=payload)
    response = price.json()
    
    #
    pricing = response['Data']['PricingDetails']
    for k,v in pricing.items():
        if k == 'Rw_Price_Float':
            print(k,v)
            priceFloat_key.append(k)
            prices_float.append(v)
        if k == 'Fractional_Price':
            print(k,v)
            priceFraction_key.append(k)
            prices_fraction.append(v)
            
    print()
    # Price Request timestamp
    time = response['Data']['TimeStamp']
    timestamps.append(time)
    print(time)
        
#Create DataFrame including all above features and randomly generated data
raw = pd.DataFrame ({'Property':priceFloat_key,'Price':prices_float,'Clients':cs})
rounded = pd.DataFrame ({'Property':priceFraction_key,'Price':prices_fraction,'Clients':cs})
metadata_2 = pd.DataFrame ({'Client-Keys':cs,'Price-Request-Timestamp':timestamps})


# plot
fig, ax = plt.subplots()
plt.style.use('ggplot')
fig.suptitle('Client Decimal Price Rounded Analysis')
#
ax.plot(rounded.Price)
ax.scatter(x=rounded.Clients, y=rounded.Price)
ax.set_xlabel('Client')
ax.set_ylabel('Rounded-Price')
#
plt.xticks(rotation=90)
plt.show()
