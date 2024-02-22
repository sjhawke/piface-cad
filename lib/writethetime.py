#!/usr/bin/env python3
"""
Methods to assist the display of the time in words
"""

NUMBER_HASH = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
              11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
              19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
              50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
              90: 'Ninety', 0: 'Twelve'}

MAX_LENGTH = 29  # tuned to ensure that we don't ever wrap to 3 lines

def write_number_as_words(number):
    """
    writes a number for the time as words
    """
    try:
        return NUMBER_HASH[number]
    except KeyError:
        try:
            return (NUMBER_HASH[number - number % 10] +
                    "-" + NUMBER_HASH[number % 10].lower())
        except KeyError:
            return 'Number out of range'


def get_am_pm_indicator(hour, minute):
    """
    generate the am/pm indicator
    """
    # pylint: disable=R0911 # allow more returns to make code clearer
    if hour == 0 and minute < 31:
        return ""
    if hour == 12 and minute < 31:
        return ""
    if hour == 23 and minute > 30:
        return ""
    if hour == 11 and minute > 30:
        return ""
    if minute > 30:
        hour = hour + 1
    if hour > 23:
        return " AM"
    if hour > 11:
        return " PM"
    return " AM"


def get_12_hour_clock_value(hour, minute):
    """
    generate the 12 hour clock value
    """
    if minute > 30:
        hour = hour + 1
    if hour in (0, 24):
        return "Midnight"
    if hour == 12:
        return "Midday"
    if hour > 12:
        return write_number_as_words(hour - 12)
    return write_number_as_words(hour)


def get_minute_text(minute):
    """
    generate the minute text
    """
    if minute  in (15, 45):
        return "Quarter"
    if minute == 30:
        return "Half"
    if minute > 30:
        return write_number_as_words(60 - minute)
    return write_number_as_words(minute)


def get_minute_indicator(minutes):
    """
    generate the minute indicator
    """
    if minutes in (15, 30, 45):
        return ""
    if minutes in (1, 59):
        return " Min"
    return " Mins"


def get_time_as_words(date_time_value):
    """
    generate the time as words
    """

    hour = date_time_value.hour
    minute = date_time_value.minute

    hour_text = get_12_hour_clock_value(hour, minute)
    minute_text = get_minute_text(minute)
    mins = get_minute_indicator(minute)
    ampm = get_am_pm_indicator(hour, minute)

    if minute == 0:
        if hour in (0, 12):
            return hour_text
        return hour_text + " O'Clock" + ampm
    if minute > 30:
        result = minute_text + mins + " To " + hour_text + ampm
        if len(result) > MAX_LENGTH:
            result = minute_text + " To " + hour_text + ampm
        return result
    result = minute_text + mins + " Past " + hour_text + ampm
    if len(result) > MAX_LENGTH:
        result = minute_text + " Past " + hour_text + ampm
    return result
