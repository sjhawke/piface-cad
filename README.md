# piface-cad

My mucking around area with code to work with the PiFace Control and Display modules on the Raspberry Pi Model B.

 ![Pi Clock Photo](https://github.com/sjhawke/piface-cad/raw/master/pi-clock.PNG)

This should work out of the box with the latest Raspbian distro, plus the PiFace CAD tools from here:

http://www.piface.org.uk/guides/setting_up_pifacecad/installing_pifacecad_package/

You will also need to generate and API key for api.openweathermap.org and find their unique number for your town/city.
Put the key into the key = "" field in the weather.py file and edit the uri to use your location code.

** Warning ** 

Python is not my language of choice professionally and the code may not be either elegant nor efficient.

Comments are welcome.

# Getting Started

 I have used a virtual environment to control dependencies, you can do the same as follows:

 To create the virtual Python3 environment:

 $ virtualenv -p python3 venv

To activate it:

 $ . ./venv/bin/activate

Now, when you run Python 3 you are actually running it from within the ./venv/bin/ folder (but you knew that already).
Your specific dependencies are now controlled for this application alone.

 $ pip install --upgrade pip
 
 $ pip install -r requirements.txt

Right now, this just restores the 'Beautiful Soup 4' library that I am using to parse web pages I want data from.

To save your libraries if you added more with pip use:

pip freeze > requirements.txt

Then make sure you check in the change!

When you are all done, run the following to get back to your usual global Python3 environment.

 $ ./venv/bin/deactivate
