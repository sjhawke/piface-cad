#!/usr/bin/env python3

import datetime
import time
import sys
import select
import os

import pifacecad
from lib import writethetime

cad = pifacecad.PiFaceCAD()
lcd = cad.lcd

listener = pifacecad.SwitchEventListener(chip=cad)


#def getDisplayTime(dateTime):
	# thedate = datetime.datetime.now()
	#return dateTime.strftime("  [  %H:%M  ]  ")
	

#def getDisplayDate(dateTime):
	# thedate = datetime.datetime.now()
	#return dateTime.strftime("%a %d-%b-%Y")


def init(display):
	display.clear()
	display.blink_off()
	display.cursor_off()
	display.backlight_on()

def clear(display):
	display.clear()
	display.backlight_off()

def button_press(event):
	print (event.pin_num)

def unregister_buttons(buttonlistener):
	buttonlistener.deactivate()

def register_buttons(buttonlistener):
	for i in range(8):
		buttonlistener.register(i, pifacecad.IODIR_FALLING_EDGE, button_press)
	buttonlistener.activate()

def main():
	# reset the screen.
	init(lcd)
	# register events
	#register_buttons(listener)
	# initialise the previous state variable.
	oldclocktime = ""
	# loop
	stopping = False

	while not stopping:
		thedate = datetime.datetime.now()
		clocktime = writethetime.getTimeAsWords(thedate)
		clocktime_lines = textwrap.wrap(clocktime,width=16)
		if (len(clocktime_lines) > 1):
				clocktime = clocktime_lines[0] + '\n' + clocktime_lines[1]
		else:
				clocktime = clocktime_lines[0]
		print (clocktime)
		if oldclocktime != clocktime:
			lcd.clear()
			oldclocktime = clocktime
			#clockdate = getDisplayDate(thedate)
			lcd.write(clocktime)

		# check for a keypress and exit if a key is pressed
		if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			break

		time.sleep(100)

	print("terminating")
	clear(lcd)
	#unregister_buttons(listener)

if __name__ == "__main__":
	main()
