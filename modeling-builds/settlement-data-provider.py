# IMPORT LIBRARIES
import json # Python built-in package json for encoding and decoding JSON data.
import requests # library for working with HTTP requests in Python
import pandas as pd # Analytics
import numpy as np # Heavy Numerical Computations
from datetime import datetime # datetime
import time

# Fixtures (retrieved form internal database manually)
fixtures = [190991,110997,190199,192001,091004]

# Data Structures (deployed in our model (note python lists will hold the order of our data)
games, elapsed_times, request_sent_times, status_codes = ([] for i in range(4))


# MODELLING-BUILD-ONE
for value in fixtures:
    #
    print("------------------------------------------------------------------------------------------------------------------")
    print("FIXTURE : {}".format(value))
    
    # safety threshold
    if len(fixtures) > 20:
        print("Too many fixtures being inputted into program. Please only add 20 fixtures to our fixture list for settlement resends (RISK-AVERSE)")
        break        
    #
    else:
        # build string/url parameter using list of values & manual input required query paramaters
        string = "https://private-hiddden-endpoint?key=x12xv&fixtureId={}&pushSettlement=true&userId=1234&source=xv" # {} acts as a placeholder
        string = string.format(value) # format() method formats the specified value(s) and insert them inside the string's placeholder
        url = (string)
        try:
            #
            dt_request = datetime.now() # Getting the current date and time request executed/processes (time will be close to time server was hit for request)
            print(dt_request)
            response = requests.get(url,timeout=(50,50)) # get requests & tiemout paranater values (seconds,seconds)
            
            #
            games.append(value) # append (add) items to data structure (empty list)
            request_timestamp = datetime.timestamp(dt_request) # Getting the timestamp (time will be close to time server was hit for request)
            request_sent_times.append(dt_request) # append date/time server request to empty list
            print("Server Request Time Sent :", request_timestamp)
            print(url)
            print("Request-Status-Code : {}".format(response.status_code)) # get request status code
            status_codes.append(response.status_code)
            #
            
            #
            print()
            print("Requests-Elapsed-Time-Property-Server-Repsonse-Time-Seconds",response.elapsed.total_seconds()) # requests property elapsed returns delta between request sent and response receieved
            seconds = response.elapsed.total_seconds()
            elapsed_times.append(seconds)
            print()
            
            # Convert api get request body to JSON object (we can anlyse the object if needed)
            data = response.json() # convert to JSON (we dont need this for settlement however will leave here in event we want to take a look at repsonse body)
            
            #
            time.sleep(10) # function takes a float argument representing the number of seconds that the program will pause for continuing
            print("sleep-function-passed")
            print("------------------------------------------------------------------------------------------------------------------")
        # Exception Handling
        # requests Connection error handling
        except requests.exceptions.ConnectionError as error:
            print("Connetion Error Raised")
            raise SystemExit(error)
        # requests HTTP status error handling
        except requests.exceptions.HTTPError as error:
            print("HTTP Error Raised")
            raise SystemExit(error)
        # request TIMEOUT error handling
        except requests.exceptions.Timeout as error:
            print("Timeout Error Raised")
            raise SystemExit(error)
            
            
#Create DataFrame including all above features and randomly generated data
df = pd.DataFrame ({'Fixture':games,'TimeTaken':elapsed_times,'SettlementSentUTC':request_sent_times,'StatusCode':status_codes})
