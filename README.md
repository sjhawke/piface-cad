# piface-cad

My mucking around area with code to work with the PiFace Control and Display modules on the Raspberry Pi Model B.

 ![Pi Clock Photo](https://github.com/sjhawke/piface-cad/blob/main/pi-clock.PNG)

This should work out of the box with the latest Raspbian distro, plus the PiFace CAD tools from here:

http://www.piface.org.uk/guides/setting_up_pifacecad/installing_pifacecad_package/

You will also need to generate an API key for api.openweathermap.org and find their unique number for your town/city,
plus the latitude and longitude for your location. These are needed for weather outlook and UV index requests.
Put the details in the startclock.sh file environment vars and run that to ensure the lib/writetheweather.py file has
the values it requires.

** Warning ** 

Python is not my language of choice professionally and the code may not be either elegant nor efficient.

Comments are welcome.

## Raspbian Note

This was originally built on the original distro that came with the Raspberry Pi Model B v1. 
It has since been updated after upgrading the operating system on my Pi to Debian (Raspbian) Bullseye. 

On newer versions of Raspbian the PiFace libraries are no longer part of the distribution, so you
will need to build them yourself from source. See [here](https://github.com/piface/pifacecad?tab=readme-ov-file#install-on-raspbian-strech-and-raspberrypi-3) for instructions.

## Getting Started

 I have used a virtual environment to control dependencies, you can do the same as follows:

 To create the virtual Python3 environment:
```
 $ python3 -m venv venv
```
To activate it:
```
 $ . ./venv/bin/activate
```
Now, when you run Python 3 you are actually running it from within the ./venv/bin/ folder (but you knew that already).
Your specific dependencies are now controlled for this application alone.

```
 $ pip install --upgrade pip
 
 $ pip install -r requirements.txt
```
Right now, this just restores the 'Beautiful Soup 4' library that I am using to parse web pages I want data from and pytest for unit testing.

To save your libraries if you added more with pip use:
```
pip freeze > requirements.txt
```
Then make sure you check in the change!

When you are all done, run the following to get back to your usual global Python3 environment.
```
 $ ./venv/bin/deactivate
```
