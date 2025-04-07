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

I2C_ADDRESS = 0x23
CMD_CONT_HIGH_RES_MODE = 0x10  # Corresponds to register 0x10


def read_lux(bus):
    # Write measurement command
    bus.write_byte(I2C_ADDRESS, CMD_CONT_HIGH_RES_MODE)
    sleep(0.02)  # 20ms delay (sensor needs this time to measure)

    # Read 2 bytes of data
    data = bus.read_i2c_block_data(I2C_ADDRESS, CMD_CONT_HIGH_RES_MODE, 2)
    raw = (data[0] << 8) | data[1]
    lux = raw / 1.2  # Convert to lux
    return lux


def main():
    with SMBus(1) as bus:  # I2C bus 1 is default on Raspberry Pi
        while True:
            lux = read_lux(bus)
            print(f"LUX: {lux:.2f} lx")
            sleep(0.5)  # 500ms delay


if __name__ == "__main__":
    main()
