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
response = ws.devices

x = json.dumps(response)
#print(x)

y = json.loads(x)
#print(y[0]["modules"][0]["dashboard_data"]["Temperature"])

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


readable_last_message = datetime.datetime.fromtimestamp(last_message).isoformat()
readable_last_seen = datetime.datetime.fromtimestamp(last_seen).isoformat()
readable_time_utc = datetime.datetime.fromtimestamp(time_utc).isoformat()
readable_date_min_temp = datetime.datetime.fromtimestamp(date_min_temp).isoformat()
readable_date_max_temp = datetime.datetime.fromtimestamp(date_max_temp).isoformat()

print(module_name)
print(battery_percent)
print(reachable)
print(readable_last_message)
print(readable_last_seen)
print(temperature)
print(readable_time_utc)
print(time_utc)
print(min_temp)
print(max_temp)
print(readable_date_min_temp)
print(readable_date_max_temp)
print(temp_trend)

#readable_time_utc = datetime.datetime.fromtimestamp(time_utc).isoformat()
#print(readable_time_utc)
#readable_time_ute = datetime.datetime.fromtimestamp(time_utc).isoformat()
#print(readable_time_utc)

#print(response)



# Comment // tripple works as multiline comment (when not assigned)
"""
file = open('response.json',"r")

data = json.load(file)

for i in data['modules']:
        print(i)

for j in i['Temperature']:
        print(j)

file.close()
"""

# Get list


# # Format list values

# Append values to JSON file

# close file

# Check if temp is within bounds

# If not send POST req to sysman


#import datetime
#readable = datetime.datetime.fromtimestamp(1613792951).isoformat()
#print(readable)
# 2021-02-20T04:49:11+01:00 // Output
