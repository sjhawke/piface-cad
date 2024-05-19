#!/usr/bin/env python3

""" Methods to assist the display of the weather in words """

import os
import requests
import requests.exceptions

def get_weather_as_words():
    """
    Get the weather as words from OpenWeatherMap
    """
    # pylint: disable=R0914

    # Settings for your API key and location details read from environment strings, e.g. exports etc
    appid = str(os.environ.get('apikey'))
    locid = str(os.environ.get('locationkey'))
    lat = str(os.environ.get('lat'))
    lon = str(os.environ.get('lon'))

    uri = ("https://api.openweathermap.org/data/2.5/weather?id="
           + locid  + "&units=metric&APPID=" + appid)
    # print(uri)
    weather = "no weather data"
    try:
        result = requests.get(uri, timeout=5)
        #print (str(r.status_code))
        if result.status_code == 200:
            # get count - check for zero and return amber.
            body = result.json()
            weather_data = body['weather']
            main = body['main']
            temp = int(round(main['temp'],0))
            outlook = weather_data[0]['description']
            weather = str(temp) + "C "  + str(main['humidity'])  + "%Hu " + outlook

        uv_uri = ("https://api.openweathermap.org/data/2.5/uvi?lon="
                  + lon  + "&lat=" + lat + "&APPID=" + appid)
        # print(uv_uri)
        uvindex = ''
        uvreq = requests.get(uv_uri, timeout=5)
        if uvreq.status_code == 200:
            body = uvreq.json()
            uv_level = body['value']
            if uv_level>8.0:
                uvindex = 'VH'
            elif uv_level>5.0:
                uvindex = "H"
            elif uv_level>2.0:
                uvindex = "M"
            else:
                uvindex = "L"
        weather = (str(temp) + "C "  + str(main['humidity'])
                   + "%Hu " + "UV:" + uvindex + "\n" + outlook)
    except requests.exceptions.HTTPError as errh: # pylint: disable=W0612
        # print("HTTP Error")
        pass
        # we swallow all communication errors
    return weather

if __name__ == '__main__':
    print(get_weather_as_words())
