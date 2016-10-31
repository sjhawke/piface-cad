#!/usr/bin/env python3

import unittest
import time
import datetime
import sys
import select
import os
import re

from lib import writethetime


class TestGetTimeAsWords(unittest.TestCase):
    def testMidnight(self):
        dt = datetime.datetime(2016,2,28,0,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Midnight")
    def testOneAm(self):
        dt = datetime.datetime(2016,2,28,1,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "One O'Clock AM")

    def testTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Two O'Clock AM")

    def testFivePastTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,5,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Five Mins Past Two AM")

    def testQuarterPastTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,15,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter Past Two AM")
                         
    def testMidday(self):
        dt = datetime.datetime(2016,2,28,12,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Midday")

    def testHalfPastTwoPm(self):
        dt = datetime.datetime(2016,2,28,14,30,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Half Past Two PM")

    def testHalfPastMidday(self):
        dt = datetime.datetime(2016,2,28,12,30,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Half Past Midday")
                         
    def testTwelveFortyFivePM(self):
        dt = datetime.datetime(2016,2,28,12,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To One PM")
    
    def testElevenFortyFivePM(self):
        dt = datetime.datetime(2016,2,28,23,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To Midnight")
                    
    def testElevenFortyFiveAM(self):
        dt = datetime.datetime(2016,2,28,11,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To Midday")

    def testTenFourteenPM(self):
        dt = datetime.datetime(2016,2,28,22,14,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Fourteen Mins Past Ten PM")


    def testTenThirtyFivePM(self):
        dt = datetime.datetime(2016,2,28,22,35,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Twenty-five Mins To Eleven PM")

    def testTenThirtyThreePM(self):
        dt = datetime.datetime(2016,2,28,22,33,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Twenty-seven To Eleven PM")

    def testElevenFiftyNinePM(self):
        dt = datetime.datetime(2016,2,28,23,59,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "One Min To Midnight")
                         
    def testMidnightandOneMin(self):
        dt = datetime.datetime(2016,2,28,0,1,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "One Min Past Midnight")
    
    def testVeryLongString(self):
        dt = datetime.datetime(2016,2,28,11,27,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Twenty-seven Past Eleven AM")

class TestWrap16x2(unittest.TestCase):
    def testTextWrappingTwoLines(self):
        text = "I am a long string that you must wrap"
        result = writethetime.wrap16x2(text)
        #           1234567890123456
        expected = "I am a long\nstring that you\nmust wrap"
        self.assertEqual(expected, result)

    def testTextWrappingOneLine(self):
        text = "short string"
        result = writethetime.wrap16x2(text)
        expected = "short string"
        self.assertEqual(expected, result)
        
    def testTextWrappingTwoLinesOverLength(self):
        text = "Twenty-seven Past Eleven AM"
        result = writethetime.wrap16x2(text)
        #           1234567890123456
        expected = "Twenty-seven\nPast Eleven AM"
        self.assertEqual(expected, result)

    def testVerifyAllTimes(self):
        for hour in range(0,24):
            for minute in range(0,60):
                dt = datetime.datetime(2016, 2, 28, hour, minute, 0)
                wtt = writethetime.getTimeAsWords(dt)
                wrap = writethetime.wrap16x2(wtt)
                array = re.split('\n', wrap)
                lines = len(array)
                self.assertTrue(3 > \
                        lines, \
                        "Count of lines is 3 or more " + \
                                        str(lines) + \
                                        " for time " + \
                                        str(hour) + \
                                        " : " + \
                                        str(minute) + " : " + \
                                        wrap)


if __name__ == '__main__':
    unittest.main()