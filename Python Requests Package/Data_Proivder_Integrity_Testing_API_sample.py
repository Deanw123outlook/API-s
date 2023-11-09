# Program - Service Provider Data Intergrity Testing Environment

import json # Python built-in package json for encoding and decoding JSON data.
import requests # library for working with HTTP requests in Python
import pandas as pd
import numpy as np
from datatime import datetime

# list of data (values) to check 
values = [1234,4678,891011,11121314] # list data structure (maintain order of our data)

#
for value in values:
    #
    print("------------------------------------------------------------------------------------------------------------------")
    print("data_id : {}".format(value))
    
    # build stings using list of values 
    string = "https://api/getserviceproviderdata?id={}&Key=xxx" # {} acts as string placeholder
    string = string.format(value) # format() method formats the specified value(s) and insert them inside the string's placeholder.
    
    # build URL parameters
    url = (string)
    response = requests.get(url) # get request
    dt_request = datetime.now() # Getting the current date and time request executed/processes (time will be close to time server was hit for request)
    timestamp = datetime.timestamp(dt_request) # Getting the timestamp (time will be close to time server was hit for request)
    print("Request-Status-Code : {}".format(response.status_code)) # get request status code
    print("Server Request Date | Time :", dt_request)
    print(url)
    
    # Convert api get request body to JSON object
    data = response.json() # convert to JSON 

    empty_dict = {}
    for x,y in data.items(): # items() method will return each item in a dictionary, as tuples in a list
        empty_dict[x] = y
    print()
    print(empty_dict['DataProviderInpuTimeStampUTC'])
    print()
    print(empty_dict['DataProviderKey'])
