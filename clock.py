#!/usr/bin/env python3
"""
Clock - main program for managing the Clock Display via the PiFaceCAD library.
"""

import datetime
import time
import socket

import pifacecad                                      # pylint: disable=E0401
import lib.writethetime as writethetime               # pylint: disable=R0402
import lib.writethedate as writethedate               # pylint: disable=R0402
import lib.lcdtextprocessing as lcdtextprocessing     # pylint: disable=R0402
import lib.writetheweather as writetheweather         # pylint: disable=R0402

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
    ip_socket.connect(("8.8.8.8", 80))
    return ip_socket.getsockname()[0]


def show_ip_address(display):
    """
    Show the IP Address of the Pi on the display.
    """
    my_ip_address = get_ip_address()
    display.clear()
    display.write("  IP ADDRESS: \n " + my_ip_address)
    time.sleep(10)

def main():
    """
    Entry point. Run the app with the main loop.
    """
    # reset the screen.
    init(lcd)
    # show ip address for a short time for maintenance and support
    show_ip_address(lcd)
    # register events
    # initialise the state variable.
    old_text = ""

    # loop forever
    stopping = False
    while not stopping:
        date_now = datetime.datetime.now()

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
            #print(text)
            #print("+--------+-----+")

        # check for a keypress and exit if a key is pressed
        # if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        #	break

        time.sleep(5)

    # print("terminating")
    clear(lcd)


# unregister_buttons(listener)

if __name__ == "__main__":
    main()
