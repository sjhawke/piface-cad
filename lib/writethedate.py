#!/usr/bin/env python3

import unittest
import time
import datetime
import sys
import select
import os


ordinalHash = { 1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth', 5: 'Fifth',
                6: 'Sixth', 7: 'Seventh', 8: 'Eighth', 9: 'Ninth', 10: 'Tenth',
               11: 'Eleventh', 12: 'Twelfth', 13: 'Thirteenth', 14: 'Fourteenth',
               15: 'Fifteenth', 16: 'Sixteenth', 17: 'Seventeenth', 18: 'Eighteenth',
               19: 'Nineteenth', 20: 'Twentieth', 21: 'Twenty-First',
               22: 'Twenty-Second', 23: 'Twenty-Third', 24: 'Twenty-Fourth',
               25: 'Twenty-Fifth', 26: 'Twenty-Sixth', 27: 'Twenty-Seventh',
               28: 'Twenty-Eighth', 29: 'Twenty-Ninth', 30: 'Thirtieth',
               31: 'Thirty-First' }

shortOrdinalHash = {  1: '1st', 
                      2: '2nd', 
                      3: '3rd', 
	             21: '21st',
                     22: '22nd', 
                     23: '23rd', 
                     31: '31st' }


monthsHash = { 1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
           6:'June', 7:'July', 8:'August', 9:'September', 10: 'October',
           11:'November', 12:'December' }

def writedayordinalaswords(number):
    try:
        return ordinalHash[number]
    except KeyError:
        return 'Number out of range'


def writeshortdayordinalaswords(number):
    try:
        return shortOrdinalHash[number]
    except KeyError:
        return str(number) + "th"


def writemonthastext(number):
    try:
        return monthsHash[number]
    except KeyError:
        return 'Number out of range'


def writedayname(dateTime):
	return dateTime.strftime("%a")


def getDateAsWords(dateTime):
    maxLength = 29  # tuned to ensure that we don't ever wrap to 3 lines
    return writedayname(dateTime) + ' ' + writeshortdayordinalaswords(dateTime.day) + ' of ' + writemonthastext(dateTime.month)
