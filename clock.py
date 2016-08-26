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


def init(display):
	display.clear()
	display.blink_off()
	display.cursor_off()
	display.backlight_on()


def clear(display):
	display.clear()
	display.backlight_off()


def button_press(event):
	temp = 1
	#print (event.pin_num)


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
	# initialise the state variable.
	oldtext = ""
	
	# loop forever
	stopping = False
	while not stopping:
		datenow = datetime.datetime.now()
		timeastext = writethetime.getTimeAsWords(datenow)
		text = writethetime.wrap16x2(timeastext)
		if oldtext != text:
			lcd.clear()
			oldtext = text
			lcd.write(text)
			#print(text)
			#print("+--------+-----+")

		# check for a keypress and exit if a key is pressed
		#if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
		#	break

		time.sleep(10)

	#print("terminating")
	clear(lcd)
	#unregister_buttons(listener)

if __name__ == "__main__":
	main()
