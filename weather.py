#!/usr/bin/env python3


# . ./venv/bin/activate
# pip install -r requirements.txt
# pip freeze > requirements.txt
# ./venv/bin/deactivate

import requests
import time

# Fleet
key= "api-key-here"
uri = "http://api.openweathermap.org/data/2.5/group?id=2649322&units=metric&APPID=" + key

try:
    r = requests.get(uri, timeout=5)
    print (str(r.status_code))
    if r.status_code == 200:
        # get count - check for zero and return amber.
        temp = r.json()['main']['temp']
        print(str(temp) +"C")


except:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp + ' - error caught interrogating ' +
          self.lastrequesturi)
    pass
    # we swallow all communication errors

