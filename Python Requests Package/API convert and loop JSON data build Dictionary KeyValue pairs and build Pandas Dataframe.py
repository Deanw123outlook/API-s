import requests # library for working with HTTP requests in Python
import pandas as pd # pandas for complex analytics
import numpy as np # numerical computations (heavy compute power)
from datetime import datetime # import datetime from datetime library
import time # import time module

clients = ["xxx_key_xxx"] # client key
d = {} # initiate empty dictionary
cs = [] # intiate empty list

for client in clients:
    print("-----------------------------------------------------------------------------------------------------------------")
    #
    string = 'http_endpoint_{}' # {} acts as string placeholder
    url = string.format(client) # # format() method formats the specified value(s) and insert them inside the string's placeholder.
    print(url)
    
    #
    response = requests.get(url) # get request
    data = response.json() # convert to JSON 
    
    # metadata
    dt_request_sent = datetime.now() # Getting the current date and time request executed/processes (time will be close to time server was hit for request)
    timestamp = datetime.timestamp(dt_request_sent) #  Timestamp (time will be close to time server was hit for request)
    print("Server-Request-Date|Time(UTC) :", dt_request_sent)
    cs.append(client)
    print("Client: ",client)
    
    #
    for i in range(len(data['PayLoad']['MCVs'])): # range method (start,stop,step)
        d["{}".format(data['PayLoad']['MCVs'][i]['Area'])] = data['PayLoad']['MCVs'][i]['Basketball'] # declare dictionary key value pairs based on data (looping JSON data)
    print("-----------------------------------------------------------------------------------------------------------------")

# dataset market over-rides
dataset = pd.DataFrame(d)
dataset = dataset.rename_axis('MCVs').reset_index()

# metadata
metadata = pd.DataFrame({'Client-Key':cs,'Request-Timestamp-UTC':dt_request_sent,'Endpoint':url})
