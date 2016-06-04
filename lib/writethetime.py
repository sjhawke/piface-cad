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
            90: 'Ninety', 0: 'Twelve'}


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
    clocktime = ""
    clocktime_lines = textwrap.wrap(text, width = line_length)
    if (len(clocktime_lines) > 2):
        clocktime = clocktime_lines[0] + '\n' + \
                    clocktime_lines[1] + '\n' + \
                    clocktime_lines[2]
    elif (len(clocktime_lines) > 1):
        clocktime = clocktime_lines[0] + '\n' + \
                    clocktime_lines[1]
    else:
        clocktime = clocktime_lines[0]
    return clocktime

def getAmPm(hour,minute):
    if (hour==0 and minute<31):
        return ""
    if (hour==12 and minute<31):
        return ""
    if (hour==23 and minute>30):
        return ""
    if (hour==11 and minute >30):
        return ""
    if (minute > 30):
        hour = hour + 1
    if (hour > 23):
        return " AM"
    if (hour > 11):
        return " PM"
    return " AM"

def get12Hour(hour,minute):
    if(minute > 30):
        hour = hour + 1
    if (hour == 0 or hour == 24):
        return "Midnight"
    if (hour == 12):
        return "Midday"
    if (hour > 12):
        return writenumberaswords(hour - 12)
    else:
        return writenumberaswords(hour)

def getMinuteText(minute):
    if(minute==15 or minute==45):
        return "Quarter"
    if(minute==30):
        return "Half"
    if(minute>30):
        return writenumberaswords(60-minute)
    else:
        return writenumberaswords(minute)

def getMinsIndicator(minutes):
    if (minutes==15 or minutes==30 or minutes==45):
        return ""
    if (minutes==1 or minutes==59):
        return " Min"
    else:
        return " Mins"

def getTimeAsWords(dateTime):
    hour = dateTime.hour
    minute = dateTime.minute

    hourText   = get12Hour(hour,minute)
    minuteText = getMinuteText(minute)
    mins       = getMinsIndicator(minute)
    ampm       = getAmPm(hour,minute)

    if (minute == 0):
        if (hour == 12 or hour == 0):
            return hourText
        else:
            return hourText + " O'Clock" + ampm
    if (minute > 30):
        result = minuteText + mins + " To " + hourText + ampm
        if (len(result) > 16):
            result = minuteText + " To " + hourText + ampm
        return result
    else:
        result = minuteText + mins + " Past " + hourText + ampm
        if (len(result) > 16):
            result = minuteText + " Past " + hourText + ampm
        return result
