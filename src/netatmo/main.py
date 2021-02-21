#! /usr/bin/env python3

import netatmo
import fs

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


    
#import datetime
#readable = datetime.datetime.fromtimestamp(1613792951).isoformat()
#print(readable)
# 2021-02-20T04:49:11+01:00
