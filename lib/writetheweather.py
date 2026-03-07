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
    appid = os.environ.get('apikey', '')
    locid = os.environ.get('locationkey', '')
    lat = os.environ.get('lat', '')
    lon = os.environ.get('lon', '')

    uri = ("https://api.openweathermap.org/data/2.5/weather?id="
           + locid + "&units=metric&APPID=" + appid)
    weather = "no weather data"
    try:
        result = requests.get(uri, timeout=5)
        if result.status_code == 200:
            body = result.json()
            weather_data = body['weather']
            main = body['main']
            temp = int(round(main['temp'], 0))
            outlook = weather_data[0]['description']

            uvindex = ''
            uv_uri = ("https://api.openweathermap.org/data/2.5/uvi?lon="
                      + lon + "&lat=" + lat + "&APPID=" + appid)
            uvreq = requests.get(uv_uri, timeout=5)
            if uvreq.status_code == 200:
                uv_level = uvreq.json()['value']
                if uv_level > 8.0:
                    uvindex = 'VH'
                elif uv_level > 5.0:
                    uvindex = "H"
                elif uv_level > 2.0:
                    uvindex = "M"
                else:
                    uvindex = "L"

            weather = (str(temp) + "C " + str(main['humidity'])
                       + "%Hu " + "UV:" + uvindex + "\n" + outlook)
    except requests.exceptions.RequestException:
        pass  # we swallow all communication errors
    return weather

if __name__ == '__main__':
    print(get_weather_as_words())
