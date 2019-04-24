#
# api.py contains a set of core functions
#

import smbus

from ht16k33.map import *
from ht16k33.register import *

class HT16K33(object):
    def __init__(self):
        # i2c device address
        self.address = HT16K33_DEFAULT_ADDRESS

        # smbus object
        self.bus = smbus.SMBus(1)

    def setup(self):
        """configure the device when it first starts up"""
        self.write_byte(HT16K33_SYSTEM_SETUP, 0xFF)
        self.write_byte(HT16K33_DISPLAY_ON, 0xFF)

    def display(self, num):
        """based on the given int number, display the value on the device"""
        if num < 0:
            self.write_led(num_map['0'], num_map['0'], num_map['0'], num_map['0'])
        elif 0 <= num <= 9:
            self.write_led(num_map['0'], num_map['0'], num_map['0'], num_map[str(num)])
        elif 10 <= num <= 99:
            str_num = str(num)[:2]
            self.write_led(num_map['0'], num_map['0'], num_map[str_num[0]], num_map[str_num[1]])
        elif 100 <= num <= 999:
            str_num = str(num)[:3]
            self.write_led(num_map['0'], num_map[str_num[0]], num_map[str_num[1]], num_map[str_num[2]])
        else:
            str_num = str(num)[:4]
            self.write_led(num_map[str_num[0]], num_map[str_num[1]], num_map[str_num[2]], num_map[str_num[3]])

    def write_led(self, d0, d1, d2, d3):
        """write the 4 digit value to the device"""
        data = [d0, 0x00, d1, 0x00, 0x00, 0x00, d2, 0x00, d3, 0x00]
        self.write_block(0x00, data)

    def write_byte(self, reg, data):
        """write byte data to a given register address"""
        self.bus.write_byte_data(self.address, reg, data)

    def write_block(self, reg, data):
        """write i2c block data to a given register address"""
        self.bus.write_i2c_block_data(self.address, reg, data)
