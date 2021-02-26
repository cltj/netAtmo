#! /usr/bin/env python3

import netatmo
import fs
import requests
import json
import time
import config
import datetime

# Fetch data using ~/.netatmorc credentials
netatmo.fetch()

# Credentials as parameters
ws = netatmo.WeatherStation( {
        'client_id': config.CLIENT_ID,          
        'client_secret': config.CLIENT_SECRET,
        'username': config.USERNAME,
        'password': config.PASSWORD,
        'device': config.DEVICE_ID } )
ws.get_data()

# Store json response in response variable
response = ws.devices

# Convert from Python to JSON // Make it a string
x = json.dumps(response)

# Convert from JSON to Python dictionary
y = json.loads(x)

# Exstract values from object (dictionary)
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

# Make timestamps readable
readable_last_message = datetime.datetime.fromtimestamp(last_message).isoformat()
readable_last_seen = datetime.datetime.fromtimestamp(last_seen).isoformat()
readable_time_utc = datetime.datetime.fromtimestamp(time_utc).isoformat()
readable_date_min_temp = datetime.datetime.fromtimestamp(date_min_temp).isoformat()
readable_date_max_temp = datetime.datetime.fromtimestamp(date_max_temp).isoformat()

# Check if temp is within bounds # Set bounds # Set message
lowest = 2.5
highest = 7.5
outOfBounds = ""

if temperature > highest:
        outOfBounds = "to high"
        reportMsg = f'Warning! Temperature on sensor {module_name} is {outOfBounds} as it was meassured at {temperature}. Take nessecary action to bring the temperature back into acceptable levels. (Between 2.5 and 7.5 Celsius)'
elif temperature < lowest:
        outOfBounds = "to low"
        reportMsg = f'Warning! Temperature on sensor {module_name} is {outOfBounds} as it was meassured at {temperature}. Take nessecary action to bring the temperature back into acceptable levels. (Between 2.5 and 7.5 Celsius)'
else:
        outOfBounds = "OK"
        reportMsg = f'Temperature on sensor {module_name} is verified OK at {temperature} degrees Celsius.'

# Configure and send response to notificaiton system
toPhone = config.TO_PHONE # Set phone number
d = {"receiver" : toPhone ,"message" : reportMsg}
payloadBody = json.dumps(d) # Make it into a json

url = config.RESPONSE_URL
payload=payloadBody
headers = {
  'Ocp-Apim-Subscription-Key': config.OCP_APIM_SUBSCRIPTION_KEY,
  'Authorization': config.AUTHORIZATION,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

### Testing ###
#----------------- NetAtmo reponse -------------------#
#print(ws.devices) # Prints all json data in a string
#print(y[0]["modules"][0]["dashboard_data"]["Temperature"]) # exampleprint on how to drill down on values in obj
#print(x) #
#----------------- LIST VALUES -----------------------#
#print(str("module_Name: " + module_name)) #
#print(f'battery_percent: {battery_percent}') #
#print(f'reachable: {reachable}') #
#print("last_message: " + readable_last_message) #
#print("last_seen: " + readable_last_seen) #
#print(f'temperature: {temperature}') #
#print("time_utc: " + readable_time_utc) #
#print(f'min_temp: {min_temp}') #
#print(f'max_temp: {max_temp}') #
#print("date_min_temp: " + readable_date_min_temp) #
#print("date_max_temp :" + readable_date_max_temp) #
#print("temp_trend: " + temp_trend) #
#------------------ POST TO NOTIFY ------------------------#
#print(jsonBody) #
#print(payloadBody) #
#print(url) #
#print(payload) #
#print(headers) #
#print(response) # Should be "<Response [200]>"
#print(response.text) #