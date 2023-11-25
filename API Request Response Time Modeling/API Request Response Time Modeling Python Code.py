# import libraries
import numpy as np
import pandas as pd
import json # Python built-in package json for encoding and decoding JSON data.
import requests # library for working with HTTP requests in Python
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Model Settings
# Model Timeout Paramter values
t1 = [0.1,0.2,'Label-Test-1'] # list data structure (ordered)
t2 = [0.4,0.6,'Label-Test-2']
t3 = [0.5,0.8,'Label-Test-3']
dict = {'test_1':t1,'test_2':t2,'test_3':t3} # add list data to dictionary

# Generate list data 1 - x for each individual test 
tests=[] # empty list
request_times = [] # UTC request time (note list data structure to maintain order of our data)
elapsed_times = [] # server response time
category = []

counter = 0 # Emply counter variable which will act as our model test threhold value ie. when the model will stop running

# loop that will build test range
for i in range(1,101,1): # range(start,stop.step)
    tests.append(i) # append (add) items to list
    
# Modelling
for key,value in dict.items(): # TEST-SET (3)
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("TEST-SET : ", key)
    #
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    set_adapter = HTTPAdapter(max_retries = 3) # Build Transport Adapter, input max_retries parameter, and mount it to an existing Session:
    time = (value[0],value[1]) # connection timeout (connect,read) seconds
    
    #
    for test in tests:
        if counter < len(tests):
            counter += 1
            print("Test :",counter)
            print("Timeout-Paramter-Values : ", time)
            
            #
            with requests.Session() as session:
                session.mount(url, set_adapter)
                try:
                    #
                    response = session.get(url, timeout=time)
                    dt_request = datetime.now() # Getting the current date and time request executed/processes (time will be close to time server was hit for request)
                    request_times.append(dt_request)
                    timestamp = datetime.timestamp(dt_request) # Getting the timestamp (time will be close to time server was hit for request)
                    
                    #
                    response.raise_for_status() # check if succesfull repsonse code
                    print("Request-Status-Code : {}".format(response.raise_for_status)) # get request status code
                    print("Server Request Date | Time (UTC) : ", dt_request)
                    
                    # label
                    category.append(value[2])
                    print(value[2])
                    
                    #
                    print()
                    print("Requests-Proporty-Server-Repsonse-Time-Seconds",response.elapsed.total_seconds()) # requests property elapsed returns delta between request sent and response receieved
                    time = response.elapsed.total_seconds()
                    elapsed_times.append(time)
                    print()
                    
                    #
                except requests.exceptions.TimeoutError as error:
                    print("Timeout-Error")
                    raise SystemExit(error)    
                except requests.exceptions.ConnectionError as error:
                    print("Connetion Error Raised")
                    raise SystemExit(error)
                except requests.exceptions.HTTPError as error:
                    print("HTTP Error Raised")
                    raise SystemExit(error)
        if counter >= len(tests):
            counter = 0

# Create DataFrame using dictionariy data sturcutre and dataframe method
threshold = pd.DataFrame ({'Request Time UTC':request_times,'Server Request Response Time Seconds':elapsed_times,'Test-Label':category})
threshold.head()

# Model Evaluation
# subsetting based on categorical data (Pandas isin method)
t1 = threshold['Test-Label'].isin(['Label-Test-1'])
t1 = threshold[t1]
t2 = threshold['Test-Label'].isin(['Label-Test-2'])
t2 = threshold[t2]
t3 = threshold['Test-Label'].isin(['Label-Test-3'])
t3 = threshold[t3]
# Generate Line Plots (Subplots)
plt.style.use('ggplot')
fig, ax = plt.subplots(3, figsize = (7,10), sharey= False)
fig.suptitle('Test Set 1 - 3')
ax[0].plot(t1.index, t1['Server Request Response Time Seconds'],color = 'b', alpha = 0.3)
ax[1].plot(t2.index, t2['Server Request Response Time Seconds'], color = 'g', alpha = 0.4)
ax[2].plot(t3.index, t3['Server Request Response Time Seconds'], color = 'r', alpha = 0.4)
# x | y labels
ax[0].set_xlabel('Testing Timeout Parameter Value (0.1, 0.2)')
ax[1].set_xlabel('Testing Timeout Parameter Value (0.4, 0.6)')
ax[2].set_xlabel('Testing Timeout Parameter Value (0.5, 0.8)')
ax[0].set_ylabel('Server-Request-Response-Time-Seconds')
ax[1].set_ylabel('Server-Request-Response-Time-Seconds')
ax[2].set_ylabel('Server-Request-Response-Time-Seconds')
# Set spacing
fig.tight_layout()
plt.show()



