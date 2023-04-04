import time

from machine import Pin, I2C
from libs.ssd1306 import SSD1306_I2C


# WARNING! Pins are hardcoded
class Display:
    def __init__(self):
        self.di2c = I2C(1, sda=Pin(2), scl=Pin(3))
        time.sleep_ms(100)
        self.d = SSD1306_I2C(128, 64, self.di2c)
        self.rows = 0
        self.cols = 0


    def text(self, s, r=None, c=None):
        if r is None: r = self.rows*10
        if c is None: c = self.cols*10
        self.d.text(s, c, r)
        self.rows += 1
        if len(s) > 16: print(f"[WARN]: Text \"{s}\" is {len(s)-16} characters too long to fit on a single row")

    def show(self):
        self.d.show()

    def clear(self):
        self.rows = 0
        self.cols = 0
        self.d.fill(0)
        self.show()
