#! /usr/bin/env python3

import netatmo
import fs
import requests
import json
import time
import config
import datetime


# fetch data using ~/.netatmorc credentials
netatmo.fetch()

# credentials as parameters
ws = netatmo.WeatherStation( {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'username': config.USERNAME,
        'password': config.PASSWORD,
        'device': config.DEVICE_ID } )
ws.get_data()
#print(ws.devices)

# Store json res in response
response = ws.devices
#print(response)

# Convert from Python to JSON // Make it a string
x = json.dumps(response)
#print(x)

# Convert from JSON to Python dictionary
y = json.loads(x)
#print(y[0]["modules"][0]["dashboard_data"]["Temperature"])

#Exstract values from object
module_name = (y[0]["modules"][0]["module_name"])
battery_percent = (y[0]["modules"][0]["battery_percent"])
reachable = (y[0]["modules"][0]["reachable"])
last_message = (y[0]["modules"][0]["last_message"])
last_seen = (y[0]["modules"][0]["last_seen"])
temperature = (y[0]["modules"][0]["dashboard_data"]["Temperature"])
time_utc = (y[0]["modules"][0]["dashboard_data"]["time_utc"])
min_temp = (y[0]["modules"][0]["dashboard_data"]["min_temp"])
max_temp = (y[0]["modules"][0]["dashboard_data"]["max_temp"])
date_min_temp = (y[0]["modules"][0]["dashboard_data"]["date_min_temp"])
date_max_temp = (y[0]["modules"][0]["dashboard_data"]["date_max_temp"])
temp_trend = (y[0]["modules"][0]["dashboard_data"]["temp_trend"])


#make timestamps readable
readable_last_message = datetime.datetime.fromtimestamp(last_message).isoformat()
readable_last_seen = datetime.datetime.fromtimestamp(last_seen).isoformat()
readable_time_utc = datetime.datetime.fromtimestamp(time_utc).isoformat()
readable_date_min_temp = datetime.datetime.fromtimestamp(date_min_temp).isoformat()
readable_date_max_temp = datetime.datetime.fromtimestamp(date_max_temp).isoformat()


#print values
print(str("module_Name: " + module_name))
print(f'battery_percent: {battery_percent}')
print(f'reachable: {reachable}')
print("last_message: " + readable_last_message)
print("last_seen: " + readable_last_seen)
print(f'temperature: {temperature}')
print("time_utc: " + readable_time_utc)
print(f'min_temp: {min_temp}')
print(f'max_temp: {max_temp}')
print("date_min_temp: " + readable_date_min_temp)
print("date_max_temp :" + readable_date_max_temp)
print("temp_trend: " + temp_trend)


# Check if temp is within bounds
# Set bounds
lowest = 2.5
highest = 7.5
outOfBounds = ""

if temperature > highest:
        outOfBounds = "to high"
elif temperature < lowest:
        outOfBounds = "to low"
else:
        outOfBounds = "OK"
    
# The messages
warningMsg = f'Warning! Temperature on sensor {module_name} is {outOfBounds} as it was meassured at {temperature}. Take nessecary action to bring the temperature back into acceptable levels. (Between 2.5 and 7.5 Celcius)' 
verifiedMsg = f'Temperature on sensor {module_name} is verified OK'

# Reporting results
toPhone = config.TO_PHONE
sms_warning_body = f'"receiver": "{toPhone}", "message": "{warningMsg}"'
sms_ok_body = f'"receiver": "{toPhone}", "message": "{verifiedMsg}"'
#print(jsonBody)


if temperature < lowest or temperature > highest:
    # If TRUE send POST req to sms service
    jsonBody = "{"+sms_warning_body+"}"
    # Log values
else:
    jsonBody = "{"+sms_ok_body+"}"
    # Log values

#print(jsonBody)

url = config.RESPONSE_URL

#print(url)
payload="{\"receiver\" : \""+toPhone+"\",\r\n\"message\" : \""+verifiedMsg+"\"}"
#print(payload)
headers = {
  'Ocp-Apim-Subscription-Key': config.OCP_APIM_SUBSCRIPTION_KEY,
  'Authorization': config.AUTHORIZATION,
  'Content-Type': 'application/json'
}

#print(headers)
response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print(response.text)