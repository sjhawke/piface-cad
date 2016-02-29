#!/usr/bin/env python3

import unittest
import time
import datetime
import sys
import select
import os
import textwrap

numberHash = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
			 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
			11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
			15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
			19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
			50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
			90: 'Ninety', 0: 'Zero'}


def writenumberaswords(number):
	try:
		return numberHash[number]
	except KeyError:
		try:
			return (numberHash[number-number%10] +
			"-" + numberHash[number%10].lower())
		except KeyError:
			return 'Number out of range'


def wrap16x2(text):
	line_length = 16
	clocktime_lines = textwrap.wrap(text, width = line_length)
	if (len(clocktime_lines) > 1):
			clocktime = clocktime_lines[0] + '\n' + clocktime_lines[1]
	else:
			clocktime = clocktime_lines[0]
	return clocktime

def getAmPm(hour):
	if (hour > 11):
		return "PM"
	return "AM"

def get12Hour(hour):
	if (hour > 12):
		return hour - 12
	return hour
	

def getTimeAsWords(dateTime):
	hour = dateTime.hour
	minute = dateTime.minute
	if ((hour == 0) and (minute == 0)):
		return "Midnight"
	if ((hour == 12) and (minute == 0)):
		return "Midday"
	if (minute == 15):
		return "Quarter" + " Past " + \
				str(writenumberaswords(get12Hour(hour))) + " " + getAmPm(hour)
	if (minute == 0):
		return str(writenumberaswords(get12Hour(hour))) + " O'Clock" + " " + getAmPm(hour)
	if (minute == 30):
		return "Half" + " Past " + str(writenumberaswords(get12Hour(hour))) + \
			   " " + getAmPm(hour)
	if (minute > 30):
		if(hour == 23):
			if (minute == 45):
				return "Quarter" + " To " + \
				 "Midnight"
			else:
				return str(writenumberaswords(60-minute)) + " Mins To " + \
					   "Midnight"
		else:
			if (minute == 45):
				return "Quarter" + " To " + \
				 str(writenumberaswords(get12Hour(hour+1))) + " " + getAmPm(hour+1)
			# process countdown to the next hour
			return str(writenumberaswords(60-minute)) + " Mins To " + \
				   str(writenumberaswords(get12Hour(hour+1))) + " " + getAmPm(hour+1)
	else:
		return str(writenumberaswords(minute)) + " Mins Past " + \
			   str(writenumberaswords(get12Hour(hour))) + " " + getAmPm(hour)








