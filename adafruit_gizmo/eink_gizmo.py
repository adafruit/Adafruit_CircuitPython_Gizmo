# SPDX-FileCopyrightText: 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_gizmo.eink_gizmo`
================================================================================

Helper for the `Tri-Color E-Ink Gizmo <https://www.adafruit.com/product/4428>`_.


* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Gizmo.git"

from time import sleep

import board
import displayio
import fourwire
from adafruit_il0373 import IL0373
from adafruit_ssd1681 import SSD1681

try:
    from typing import Optional

    from busio import SPI
    from microcontroller import Pin
except ImportError:
    pass


class EInk_Gizmo(IL0373):
    """Class representing a 152x152 Tri-Color EInk Gizmo.

    :param"""

    def __init__(
        self,
        *,
        spi: Optional[SPI] = None,
        cs: Optional[Pin] = None,
        dc: Optional[Pin] = None,
        reset: Optional[Pin] = None,
        busy: Optional[Pin] = None,
    ) -> None:
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
        self._display_bus = fourwire.FourWire(
            spi, command=dc, chip_select=cs, reset=reset, baudrate=1000000
        )
        sleep(1)
        super().__init__(
            self._display_bus,
            width=152,
            height=152,
            busy_pin=busy,
            rotation=180,
            highlight_color=0xFF0000,
        )


class EInk_HD_Gizmo(SSD1681):
    """Class representing a 200x200 Tri-Color EInk HD Gizmo."""

    def __init__(
        self,
        *,
        spi: Optional[SPI] = None,
        cs: Optional[Pin] = None,
        dc: Optional[Pin] = None,
        reset: Optional[Pin] = None,
        busy: Optional[Pin] = None,
    ) -> None:
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
        self._display_bus = fourwire.FourWire(
            spi, command=dc, chip_select=cs, reset=reset, baudrate=1000000
        )
        sleep(1)
        super().__init__(
            self._display_bus,
            width=200,
            height=200,
            busy_pin=busy,
            rotation=180,
            highlight_color=0xFF0000,
        )
