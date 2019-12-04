# The MIT License (MIT)
#
# Copyright (c) 2019 Carter Nelson for Adafruit Industries
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

Helper for the `TFT Gizmo <https://www.adafruit.com/product/4367>`_.


* Author(s): Carter Nelson, Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Gizmo.git"

import board
import displayio
from adafruit_st7789 import ST7789

# pylint: disable=invalid-name, too-few-public-methods
class TFT_Gizmo(ST7789):
    """Class representing a TFT Gizmo."""

    def __init__(self, *, spi=None, cs=board.RX, dc=board.TX,
                 backlight=board.A3, rotation=180):
        displayio.release_displays()
        if spi is None:
            import busio
            spi = busio.SPI(board.SCL, MOSI=board.SDA)
        self._display_bus = displayio.FourWire(spi,
                                               command=dc,
                                               chip_select=cs)
        super().__init__(self._display_bus, width=240, height=240,
                         rowstart=80, backlight_pin=backlight,
                         rotation=rotation)
