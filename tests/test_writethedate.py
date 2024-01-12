#!/usr/bin/env python3

"""
Tests to validate the writethedate module
"""

import unittest
import datetime

from lib import writethedate, lcdtextprocessing

class TestGetTimeAsWords(unittest.TestCase):
    """
    Tests to check that the conversion to text is correct for the display of the time
    """
    def testMidnight(self):
        dt = datetime.datetime(2016, 2, 28, 0, 0, 0)
        self.assertEqual(
                writethedate.get_date_as_words(dt),
                'Sun 28th of February 2016')


    def testMidnightAndOneMinute(self):
        dt = datetime.datetime(2019, 6, 27, 0, 1, 0)
        self.assertEqual(
                     writethedate.get_date_as_words(dt),
                     'Thu 27th of June 2019')

    def testMultiLineDate(self):
        dt = datetime.datetime(2016, 2, 28, 0, 0, 0)
        text = writethedate.get_date_as_words(dt)
        ml = lcdtextprocessing.wrap_16_x_2(text=text)
        self.assertEqual(
                ml,
                '  Sun 28th of   \n February 2016  ')
#               '123456789x123456\n123456789x123456'

if __name__ == '__main__':
    unittest.main()
