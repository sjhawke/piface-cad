#!/usr/bin/env python3

import textwrap

def wrap16x2(text):
    line_length = 16
    datetext = ""
    datetext_lines = textwrap.wrap(text, width=line_length)
    if (len(datetext_lines) > 2):
        datetext = '{0: ^16}'.format(datetext_lines[0]) + '\n' + \
                   '{0: ^16}'.format(datetext_lines[1]) + '\n' + \
                   '{0: ^16}'.format(datetext_lines[2])
    elif (len(datetext_lines) > 1):
        datetext = '{0: ^16}'.format(datetext_lines[0]) + '\n' + \
                   '{0: ^16}'.format(datetext_lines[1]) 
    else:
        datetext = '{0: ^16}'.format(datetext_lines[0]) 
    return datetext
