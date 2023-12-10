# Testing API Request Time Execution Accuracy: Requests_toolbelt_lib v Datetime_module
# We want to the test which is the most accurate representation of time take to execute the request across different Python libraries abd features.

# import required libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from datetime import datetime

# PRE_DEFINE INPUTS/DATA-STRUCTURES
# Python's list data structures (maintain order of our data important for this task)
tests = []
req_library = []
dt_module = []
url = ('https://api.coindesk.com/v1/bpi/currentprice.json') # Build URL (string object)
print(type(url))
print(url)

# BUILD TEST MODEL
for test in range(1,100,1): # range (start,stop,step)
    tests.append(test)
    print("--------------------------------------------------------------")
    print("Test-Number:", test) 
    print()
    
    dt_start = datetime.now() # datetime module
    response = requests.get(url) # execute GET request
    dt_end = datetime.now() # datetime module
    time =  dt_end - dt_start # datetime module
    elap_time = response.elapsed.total_seconds() # requests elapsed time property (generated automatically on above get request)
    
    # Results
    req_library.append(elap_time)
    dt_module.append(time.total_seconds())
    
    # print output
    print("Sample T {} A").format(test)
    print(elap_time)
    print()
    print("Sample T {} B").format(test)
    print(time)
    print("--------------------------------------------------------------")
    
# Create DataFrame using dictionariy data sturcutre and dataframe method
tests = pd.DataFrame ({'Test_Number':tests,'requests_toolbelt_lib':req_library,'datetime_mod':dt_module})
tests['pct_change_lambda'] = tests[['requests_toolbelt_lib', 'datetime_mod']].apply(lambda x: ((x[1] - x[0]) / x[0]) * 100, axis=1) # create new df column - percentage change between both columns
tests.set_index("Test_Number", inplace = True) # set dataframe index
tests.head()

# DATA VISULIZATION (evaluation/analysis)
# Generate Line Plots (Subplots)
plt.style.use('ggplot')
fig, ax = plt.subplots(2, figsize = (7,10), sharey= False)
fig.suptitle('Testing Request Time Accuracy: Requests_toolbelt_library v Datetime_Module')
ax[0].plot(tests.index, tests.requests_toolbelt_lib,color = 'b', alpha = 0.3)
ax[1].plot(tests.index, tests.datetime_mod, color = 'g', alpha = 0.4)
# x | y labels
ax[0].set_xlabel('Test-Number')
ax[1].set_xlabel('Test-Number')
ax[0].set_ylabel('requests_toolbelt_lib Time Range')
ax[1].set_ylabel('datetime_mod Time Range')
# Set spacing
fig.tight_layout()
plt.show()


