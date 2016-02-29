#!/usr/bin/env python3

import unittest
import time
import datetime
import sys
import select
import os

from lib import writethetime


class TestGetTimeAsWords(unittest.TestCase):
    def testMidnight(self):
        dt = datetime.datetime(2016,2,28,0,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Midnight",
                         "expect midnight")
    def testOneAm(self):
        dt = datetime.datetime(2016,2,28,1,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "One O'Clock AM",
                         "expect 1am")

    def testTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Two O'Clock AM",
                         "expect 2am")

    def testFivePastTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,5,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Five Mins Past Two AM",
                         "expect 2:05am")

    def testQuarterPastTwoAm(self):
        dt = datetime.datetime(2016,2,28,2,15,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter Past Two AM",
                         "expect 2:15am")
                         
    def testMidday(self):
        dt = datetime.datetime(2016,2,28,12,0,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Midday",
                         "expect 12pm")

    def testHalfPastTwoPm(self):
        dt = datetime.datetime(2016,2,28,14,30,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Half Past Two PM",
                         "expect 2:30pm")

    def testHalfPastMidday(self):
        dt = datetime.datetime(2016,2,28,12,30,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Half Past Twelve PM",
                         "expect 12:30pm")
                         
    def testTwelveFortyFivePM(self):
        dt = datetime.datetime(2016,2,28,12,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To One PM",
                         "Quarter To One PM")
    
    def testElevenFortyFivePM(self):
        dt = datetime.datetime(2016,2,28,23,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To Midnight",
                         "Quarter To 12 Midnight")
                    
    def testElevenFortyFiveAM(self):
        dt = datetime.datetime(2016,2,28,11,45,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Quarter To Twelve PM",
                         "Quarter To 12 AM")

    def testTenFourteenPM(self):
        dt = datetime.datetime(2016,2,28,22,14,0)
        self.assertEqual(writethetime.getTimeAsWords(dt), 
                         "Fourteen Mins Past Ten PM")

class TestWrap16x2(unittest.TestCase):
    def testTextWrappingTwoLines(self):
        text = "I am a long string that you must wrap"
        result = writethetime.wrap16x2(text)
        #           1234567890123456
        expected = "I am a long\nstring that you"
        self.assertEqual(expected, result)

    def testTextWrappingOneLine(self):
        text = "short string"
        result = writethetime.wrap16x2(text)
        expected = "short string"
        self.assertEqual(expected, result)
