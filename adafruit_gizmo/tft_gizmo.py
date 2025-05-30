# SPDX-FileCopyrightText: 2019 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_gizmo.tft_gizmo`
================================================================================

Helper for the `TFT Gizmo <https://www.adafruit.com/product/4367>`_.


* Author(s): Carter Nelson, Melissa LeBlanc-Williams
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Gizmo.git"

import board
import displayio
import fourwire
from adafruit_st7789 import ST7789

try:
    from typing import Optional

    from busio import SPI
    from microcontroller import Pin
except ImportError:
    pass


class TFT_Gizmo(ST7789):
    """Class representing a TFT Gizmo."""

    def __init__(
        self,
        *,
        spi: Optional[SPI] = None,
        cs: Pin = board.RX,
        dc: Pin = board.TX,
        backlight: Pin = board.A3,
        rotation: int = 180,
    ) -> None:
        displayio.release_displays()
        if spi is None:
            import busio

            spi = busio.SPI(board.SCL, MOSI=board.SDA)
        self._display_bus = fourwire.FourWire(spi, command=dc, chip_select=cs)
        super().__init__(
            self._display_bus,
            width=240,
            height=240,
            rowstart=80,
            backlight_pin=backlight,
            rotation=rotation,
        )
