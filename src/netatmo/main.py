#! /usr/bin/env python3

import netatmo
import fs
import requests
import json
import time


# fetch data using ~/.netatmorc credentials
netatmo.fetch()

# credentials as parameters
ws = netatmo.WeatherStation( {
        'client_id': '<CLIENT_ID>',
        'client_secret': '<CLIENT_SECRET>',
        'username': '<USER_NAME>',
        'password': '<PASSWORD>',
        'device': '<DEVICE_ID>' } )
ws.get_data()
print(ws.devices)

# Open file 

# Get list

# Format list values

# Append values to JSON file

# close file

# Check if temp is within bounds

# If not send POST req to sysman


#import datetime
#readable = datetime.datetime.fromtimestamp(1613792951).isoformat()
#print(readable)
# 2021-02-20T04:49:11+01:00 // Output
