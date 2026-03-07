#!/usr/bin/env python3
"""
Mock/stub for the pifacecad hardware library.

Provides the same interface as pifacecad so that clock.py can run on any
machine without PiFace hardware attached. The LCD is rendered as a 16x2
bordered display in the terminal, with ANSI cursor movement so updates
overwrite the previous frame in-place.

Usage — imported automatically by clock.py when pifacecad is not available.
Can also be tested standalone::

    python -m lib.pifacecad_mock
"""

import sys


class LcdMock:
    """
    Terminal mock for the PiFace CAD LCD.
    Renders a 16x2 character display inside a border, updating in-place.
    """

    _BORDER_TOP    = "┌────────────────┐"
    _BORDER_BOTTOM = "└────────────────┘"
    _BLANK_LINE    = " " * 16

    def __init__(self):
        self._backlight = False
        self._rendered = False

    # ------------------------------------------------------------------
    # LCD control methods (no-ops on a terminal)
    # ------------------------------------------------------------------

    def blink_off(self):
        """Disable cursor blink (no-op)."""

    def cursor_off(self):
        """Disable cursor (no-op)."""

    def backlight_on(self):
        """Turn backlight on (no-op)."""
        self._backlight = True

    def backlight_off(self):
        """Turn backlight off — renders a blank display."""
        self._backlight = False
        self._render(self._BLANK_LINE, self._BLANK_LINE)

    # ------------------------------------------------------------------
    # Content methods
    # ------------------------------------------------------------------

    def clear(self):
        """Clear the display."""
        self._render(self._BLANK_LINE, self._BLANK_LINE)

    def write(self, text):
        """
        Write text to the display.

        Expects text already formatted for the LCD — lines separated by ``\\n``,
        each up to 16 characters wide (as produced by
        ``lcdtextprocessing.wrap_16_x_2``).
        """
        lines = text.split("\n")
        line1 = lines[0] if len(lines) > 0 else self._BLANK_LINE
        line2 = lines[1] if len(lines) > 1 else self._BLANK_LINE
        self._render(line1, line2)

    # ------------------------------------------------------------------
    # Internal rendering
    # ------------------------------------------------------------------

    def _render(self, line1, line2):
        if self._rendered:
            # Move the cursor back up to overwrite the previous frame.
            sys.stdout.write("\033[4A")
        print(self._BORDER_TOP)
        print(f"│{line1:16.16}│")
        print(f"│{line2:16.16}│")
        print(self._BORDER_BOTTOM, flush=True)
        self._rendered = True


class PiFaceCADMock:  # pylint: disable=too-few-public-methods
    """Mock for pifacecad.PiFaceCAD."""

    def __init__(self):
        self.lcd = LcdMock()


# Alias so this module is a drop-in replacement for pifacecad.
PiFaceCAD = PiFaceCADMock


class SwitchEventListenerMock:  # pylint: disable=too-few-public-methods
    """Mock for pifacecad.SwitchEventListener."""

    def __init__(self, chip=None):
        pass


# Alias so this module is a drop-in replacement for pifacecad.
SwitchEventListener = SwitchEventListenerMock


# ---------------------------------------------------------------------------
# Quick standalone demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import time

    print("PiFace CAD mock — demo mode")
    print()
    cad = PiFaceCADMock()
    lcd = cad.lcd
    lcd.backlight_on()
    lcd.write("  Hello, World! \n   mock LCD!   ")
    time.sleep(2)
    lcd.write("  Quarter Past  \n    Two AM     ")
    time.sleep(2)
    lcd.clear()
    lcd.backlight_off()
    print("Done.")
