# import requests
import requests
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

import pandas as pd
import numpy as np
from datetime import datetime

url = "string"
headers = {'user-agent': 'my-app/x.x.x'}
payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
set_adapter = HTTPAdapter(max_retries = 3) # Build Transport Adapter, input max_retries parameter, and mount it to an existing Session:
timeout = (0.005,0.008) # connection timeout (connect,read) seconds

# 
with requests.Session()as session:
session.mount(url, set_adapter)
    try:
        #
        response = session.get(url, headers , payload, timeout)
        dt_request = datetime.now() # Getting the current date and time request executed/processes (time will be close to time server was hit for request)
        timestamp = datetime.timestamp(dt_request) # Getting the timestamp (time will be close to time server was hit for request)
        response.raise_for_status(): # check if succesfull repsonse code
        print("Request-Status-Code : {}".format(response.raise_for_status)) # get request status code
        print("Server Request Date | Time :", dt_request)   
        print(response.status_code)
        data = response.json()
        #
    except requests.exceptions.ConnectionError as error:
        raise SystemExit(error)
    except requests.exceptions.HTTPError as error:
        raise SystemExit(error)




