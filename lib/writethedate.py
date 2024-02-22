#!/usr/bin/env python3

"""
Module for processing date into text for display on the LCD
"""

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

def write_day_ordinal_as_words(number):
    """
    Converts a given number to its corresponding ordinal word representation.

    Args:
        number (int): The number to be converted.

    Returns:
        str: The ordinal word representation of the number.

    Raises:
        KeyError: If the number is out of range.

    """
    try:
        return ordinalHash[number]
    except KeyError:
        return 'Number out of range'


def write_short_day_ordinal_as_words(number):
    """
    Converts a given number to its corresponding short ordinal word representation.

    Args:
        number (int): The number to be converted.

    Returns:
        str: The short ordinal word representation of the number.

    Raises:
        None
    """
    try:
        return shortOrdinalHash[number]
    except KeyError:
        return str(number) + "th"


def write_month_as_text(number):
    """
    Converts a month number to its corresponding text representation.

    Args:
        number (int): The month number.

    Returns:
        str: The text representation of the month or an error message.
    """
    try:
        return monthsHash[number]
    except KeyError:
        return 'Number out of range'


def write_day_name(date_time):
    """
    Returns the day of the week as a three-letter abbreviation.
    
    Args:
        dateTime (datetime): The input datetime object.
    
    Returns:
        str: The day of the week as a three-letter abbreviation.
    """
    return date_time.strftime("%a")


def get_date_as_words(date_time):
    """
    Returns the date as words for display on the LCD.
    
    Args:
        date_time (datetime): The input datetime object.
    
    Returns:
        str: The date as words.
    """
    return write_day_name(date_time) + ' ' + write_short_day_ordinal_as_words(date_time.day) + \
        ' of ' + write_month_as_text(date_time.month) + ' ' + date_time.strftime('%Y')
