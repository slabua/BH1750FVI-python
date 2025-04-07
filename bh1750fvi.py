# -*- coding: utf-8 -*-
"""BH1750FVI Ambient Light I2C Sensor
   Python Driver for the Raspberry Pi.
"""

__author__ = "Salvatore La Bua"
__copyright__ = "Copyright 2025, Salvatore La Bua"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Salvatore La Bua"
__email__ = "slabua@gmail.com"
__status__ = "Development"

from time import sleep
from smbus2 import SMBus


class BH1750FVI:
    DEFAULT_I2C_ADDR = 0x23
    CMD_CONT_HIGH_RES_MODE = 0x10

    def __init__(self, bus_num=1, address=DEFAULT_I2C_ADDR):
        self.address = address
        self.bus = SMBus(bus_num)

    def read_lux(self):
        # Write measurement command
        self.bus.write_byte(self.address, self.CMD_CONT_HIGH_RES_MODE)
        sleep(0.02)  # 20ms delay to allow sensor measurement

        # Read 2 bytes of data
        data = self.bus.read_i2c_block_data(
            self.address, self.CMD_CONT_HIGH_RES_MODE, 2
        )
        raw = (data[0] << 8) | data[1]
        return raw / 1.2  # Convert to lux

    def close(self):
        self.bus.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def main():
    with BH1750FVI() as sensor:
        while True:
            lux = sensor.read_lux()
            print(f"LUX: {lux:.2f} lx")
            sleep(0.5)


if __name__ == "__main__":
    main()
