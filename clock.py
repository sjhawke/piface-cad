#!/usr/bin/env python3

"""
Clock - main program for managing the Clock Display via the PiFaceCAD library.
"""

import datetime
import socket
import time

from zoneinfo import ZoneInfo

try:
    import pifacecad  # pylint: disable=E0401
except ImportError:
    import lib.pifacecad_mock as pifacecad  # pylint: disable=R0402

from lib import (  # pylint: disable=R0402
    lcdtextprocessing,
    writethedate,
    writethetime,
    writetheweather,
)

cad = pifacecad.PiFaceCAD()
lcd = cad.lcd

listener = pifacecad.SwitchEventListener(chip=cad)


def init(display):
    """
    Clear and initialise the display.
    """
    display.clear()
    display.blink_off()
    display.cursor_off()
    display.backlight_on()


def clear(display):
    """
    Wipe the display.
    """
    display.clear()
    display.backlight_off()


def get_ip_address():
    """
    Get IP Address of the Pi.
    """
    ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip_socket.connect(("8.8.8.8", 80))
        return ip_socket.getsockname()[0]
    finally:
        ip_socket.close()


def show_ip_address(display):
    """
    Show the IP Address of the Pi on the display.
    """
    try:
        my_ip_address = get_ip_address()
    except OSError:
        my_ip_address = "unavailable"
    display.clear()
    raw_text = "  IP ADDRESS: \n " + my_ip_address
    display.write(lcdtextprocessing.wrap_16_x_2(raw_text))
    time.sleep(10)


def main():
    """
    Entry point. Run the app with the main loop.
    """
    # reset the screen.
    init(lcd)
    # show ip address for a short time for maintenance and support
    show_ip_address(lcd)
    # initialise the state variable.
    old_text = ""

    timezone = ZoneInfo("Europe/London")

    # loop forever
    while True:
        date_now = datetime.datetime.now(timezone)

        if date_now.second < 9:
            # show time
            raw_text = writethetime.get_time_as_words(date_now)
        elif date_now.second < 19:
            # show date
            raw_text = writethedate.get_date_as_words(date_now)
        elif date_now.second < 29:
            # show weather
            raw_text = writetheweather.get_weather_as_words()
        elif date_now.second < 39:
            # show time
            raw_text = writethetime.get_time_as_words(date_now)
        elif date_now.second < 49:
            # show date
            raw_text = writethedate.get_date_as_words(date_now)
        else:
            # show weather
            raw_text = writetheweather.get_weather_as_words()

        text = lcdtextprocessing.wrap_16_x_2(raw_text)
        if old_text != text:
            lcd.clear()
            old_text = text
            lcd.write(text)

        time.sleep(5)

if __name__ == "__main__":
    main()
