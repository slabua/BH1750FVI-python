# -*- coding: utf-8 -*-
"""BH1750FVI Ambient Light I2C Sensor
   Micropython Driver for the Raspberry Pi Pico.
"""

__author__ = "Salvatore La Bua"
__copyright__ = "Copyright 2025, Salvatore La Bua"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Salvatore La Bua"
__email__ = "slabua@gmail.com"
__status__ = "Development"

from machine import I2C, Pin
from utime import sleep, sleep_ms


class BH1750FVI:
    DEFAULT_I2C_ADDR = 0x23
    CMD_CONT_HIGH_RES_MODE = 0x10

    def __init__(self, i2c=None, scl=1, sda=0, freq=100000, address=DEFAULT_I2C_ADDR):
        self.address = address
        if i2c is None:
            self.i2c = I2C(0, scl=Pin(scl), sda=Pin(sda), freq=freq)
        else:
            self.i2c = i2c

    def read_lux(self):
        self.i2c.writeto(self.address, bytes([self.CMD_CONT_HIGH_RES_MODE]))
        sleep_ms(20)  # Wait for measurement
        data = self.i2c.readfrom(self.address, 2)
        raw = (data[0] << 8) | data[1]
        return raw / 1.2


def main():
    sensor = BH1750FVI()
    while True:
        lux = sensor.read_lux()
        print("LUX: {:.2f} lx".format(lux))
        sleep(0.5)


if __name__ == "__main__":
    main()
