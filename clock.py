#!/usr/bin/env python3

import datetime
import time
import socket

import pifacecad
import lib.writethetime as writethetime
import lib.writethedate as writethedate
import lib.lcdtextprocessing as lcdtextprocessing
import lib.writetheweather as writetheweather

cad = pifacecad.PiFaceCAD()
lcd = cad.lcd

listener = pifacecad.SwitchEventListener(chip=cad)


def init(display):
    display.clear()
    display.blink_off()
    display.cursor_off()
    display.backlight_on()


def clear(display):
    display.clear()
    display.backlight_off()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def showIpAddress(display):
    ip = get_ip_address()
    display.clear()
    display.write("  IP ADDRESS: \n " + ip)
    time.sleep(10)

def main():
    # reset the screen.
    init(lcd)
    # show ip address for a short time for maintenance and support
    showIpAddress(lcd)
    # register events
    # initialise the state variable.
    oldtext = ""

    # loop forever
    stopping = False
    while not stopping:
        datenow = datetime.datetime.now()
        
        if(datenow.second < 9):
            # show time
            rawtext = writethetime.getTimeAsWords(datenow)
        elif(datenow.second < 19):
            # show date
            rawtext = writethedate.getDateAsWords(datenow)
        elif(datenow.second < 29):
            # show weather
            rawtext = writetheweather.getWeatherAsWords()
        elif(datenow.second < 39):
            # show time
            rawtext = writethetime.getTimeAsWords(datenow)
        elif(datenow.second < 49):
            # show date
            rawtext = writethedate.getDateAsWords(datenow)
        else:
            # show weather
            rawtext = writetheweather.getWeatherAsWords()

        text = lcdtextprocessing.wrap16x2(rawtext)
        if oldtext != text:
            lcd.clear()
            oldtext = text
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
