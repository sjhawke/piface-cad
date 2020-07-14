#!/usr/bin/env python3

import os
import requests
import time
import json

def getWeatherAsWords():

    # Settings for your API key and location details read from environment strings, e.g. exports etc
    appid = str(os.environ.get('apikey'))
    locid = str(os.environ.get('locationkey'))
    lat = str(os.environ.get('lat'))
    lon = str(os.environ.get('lon'))

    uri = "https://api.openweathermap.org/data/2.5/weather?id=" + locid  + "&units=metric&APPID=" + appid
    # print(uri)
    weather = "no weather data"
    try:
        r = requests.get(uri, timeout=5)
        #print (str(r.status_code))
        if r.status_code == 200:
            # get count - check for zero and return amber.
            body = r.json()
            w = body['weather']
            main = body['main']
            temp = int(round(main['temp'],0))
            outlook = w[0]['description']
            weather = str(temp) + "C "  + str(main['humidity'])  + "%Hu " + outlook

        uv_uri = "https://api.openweathermap.org/data/2.5/uvi?lon=" + lon  + "&lat=" + lat + "&APPID=" + appid
        # print(uv_uri)
        uvreq = requests.get(uv_uri, timeout=5)
        if uvreq.status_code == 200:
            body = uvreq.json()
            uv = body['value']
            uvindex = ''
            if(uv>8.0):
                uvindex = 'VH'
            elif(uv>5):
                uvindex = "H" 
            elif(uv>2.0):
                uvindex = "M"
            else:
                uvindex = "L"
        weather = str(temp) + "C "  + str(main['humidity'])  + "%Hu " + "uv" + uvindex + " " + outlook
    except:
        pass
        # we swallow all communication errors
    return weather

if __name__ == '__main__':
    print(getWeatherAsWords())
