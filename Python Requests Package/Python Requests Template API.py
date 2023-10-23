#Import requests
import requests

#Get request
response = requests.get(URL_LINK)

#Passing paramters in URLs
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('URL_LINK', params=payload)

#Passing Headers
url = 'URL_LINK'
headers = {'user-agent': 'my-app/x.x.x'}
response = requests.get(url, headers=headers)

#Response Content
print(response.text)
print(response.json())
print(response.encoding)
print(response.Headers)

#Raw Respone (Server Socket Response)
r = requests.get('URL_Link', stream = True)
print(r.raw)
print(r.raw.read(10))

#Response Status Code
r.status_code
r.raise_for_status() # returns an HTTPError object if an error has occurred during the process (debugging)

#Timeouts
time = 0.001
response = requests.get('URL_Link', timeout=time) # Timeoout stop requests waiting for a response after a given number of seconds with the timeout parameter

# CODE TEMPLATE
import requests

url = 'URL_LINK' # url link (API)
payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'} # parameters
headers = {'user-agent': 'my-app/x.x.x'} # headers
time = 0.010 # timeout

def request_func(url,params,payload,headers):
    response = requests.get(url, params = payload, headers=headers, timeout=time)
    if response.status_code == 200:
        print(response.status_code)
        data = response.json()
    else:
        print(response.status_code)
        print("Unsuccefull-Response-Code-Generated")


