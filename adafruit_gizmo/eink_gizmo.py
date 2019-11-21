# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_gizmo.tft_gizmo`
================================================================================

Helper for the `Tri-Color E-Ink Gizmo <https://www.adafruit.com/product/4428>`_.


* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Gizmo.git"

from time import sleep
import board
import displayio
from adafruit_il0373 import IL0373

# pylint: disable=invalid-name, too-few-public-methods
class EInk_Gizmo(IL0373):
    """Class representing a EInk Gizmo."""

    def __init__(self, *, spi=None, cs=None, dc=None, reset=None, busy=None):
        displayio.release_displays()
        if spi is None:
            import busio
            spi = busio.SPI(board.SCL, MOSI=board.SDA)
        if cs is None:
            cs = board.RX
        if dc is None:
            dc = board.TX
        if reset is None:
            reset = board.A3
        self._display_bus = displayio.FourWire(spi,
                                               command=dc,
                                               chip_select=cs,
                                               reset=reset,
                                               baudrate=1000000)
        sleep(1)
        super().__init__(self._display_bus, width=152, height=152,
                         busy_pin=busy, rotation=180,
                         highlight_color=0xff0000)
