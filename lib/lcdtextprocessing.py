#!/usr/bin/env python3
"""
Module to process text for 16x2 LCD display 
"""

import textwrap


def wrap_16_x_2(text):
    """
    Wrap text to 16x2 LCD display
    
    # left filling 
    print(f'{"geeks" :*>15}') 
    
    # right filling 
    print(f'{"geeks" :*<15}') 

    """
    line_length = 16
    datetext = ""
    datetext_lines = textwrap.wrap(text, width=line_length)
    if len(datetext_lines) > 2:
        datetext = f'{datetext_lines[0]: ^16}\n{datetext_lines[1]: ^16}\n{datetext_lines[2]: ^16}'
    elif len(datetext_lines) > 1:
        datetext = f'{datetext_lines[0]: ^16}\n{datetext_lines[1]: ^16}'
    else:
        datetext = f'{datetext_lines[0]: ^16}'
    return datetext
